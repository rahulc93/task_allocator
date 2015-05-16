from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.utils import timezone

import pytz
from pytz import timezone as tzone

from .forms import TaskForm

from task.models import Configuration

# Create your views here.

def index(request):
        #return HttpResponse("Hello, world. You're at the polls index.")
        task_list = Configuration.objects.all()
        context = {'task_list': task_list}
        return render(request, 'task/task.html', context)


def get_task(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            un = form.cleaned_data['user_name']
            print "User Name entered: ", un
            c = form.cleaned_data['country']
            print "Country entered: ", c
            tt = form.cleaned_data['task_type']
            print "Task type entered: ", tt
            st = form.cleaned_data['start_time']
            print "Start Time entered: ", st
            #print type(st)
            et = form.cleaned_data['end_time']
            print "End Time entered: ", et
            #print type(et)
            # set the django_timezone session key according to the user-entered value
            request.session['django_timezone'] = request.POST['timezone']
            current_tz = timezone.get_current_timezone()
            print "Currently activated Time Zone: ", current_tz
            stu = pytz.UTC.normalize(st.astimezone(pytz.UTC))
            print "Start Time UTC: ", stu
            etu = pytz.UTC.normalize(et.astimezone(pytz.UTC))
            print "End Time UTC: ", etu
            time_diff = stu - pytz.UTC.normalize(timezone.now().astimezone(pytz.UTC))
            if time_diff.seconds != 0:
                mins, secs = divmod(time_diff.total_seconds(), 60)
                hours, mins = divmod(mins, 60)
                days, hours = divmod(hours, 24)
                months, days = divmod(days, 30)
                years, months = divmod(months, 12)
                stat = ""
                if years:
                    stat += "%d years" % years
                if months:
                    stat += "%d months" % months
                if days:
                    stat += "%d days" % days
                if hours:
                    stat += "%d hours" % hours
                if mins:
                    stat += "%d minutes" % mins
                if secs:
                    stat += "%d secs" % secs
            else:
                stat = "True"
            Configuration(task_type = tt, country = c, user_name = un, start_time = st, end_time = et, timezone = request.session['django_timezone'], status = stat).save()
            #form.save()
            # redirect to a new URL:
            context = {'task_list': Configuration.objects.all()}
            return redirect('/task', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, 'task/task_entry.html', {'form': form, 'timezones': pytz.common_timezones})

def update_status(request, ident):
    entry = Configuration.objects.filter(id = ident)
    time_diff = pytz.UTC.normalize(entry.start_time.astimezone(pytz.UTC)) - pytz.UTC.normalize(timezone.now().astimezone(pytz.UTC))
    if time_diff.seconds != 0:
        mins, secs = divmod(time_diff.total_seconds(), 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        months, days = divmod(days, 30)
        years, months = divmod(months, 12)
        entry.status = ""
        if years:
            entry.status += "%d years" % years
        if months:
            entry.status += "%d months" % months
        if days:
            entry.status += "%d days" % days
        if hours:
            entry.status += "%d hours" % hours
        if mins:
            entry.status += "%d minutes" % mins
        if secs:
            entry.status += "%d secs" % secs
    else:
        status = "True"
    entry.save()
    context = {'task_list': Configuration.objects.all()}
    return redirect('/task', context)

