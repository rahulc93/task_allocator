from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

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
            print type(st)
            et = form.cleaned_data['end_time']
            print "End Time entered: ", et
            print type(et)
            request.session['django_timezone'] = request.POST['timezone']
            print "Time Zone: ", request.session['django_timezone']
            #time_zone = pytz.timezone( str( timezone.get_current_timezone_name() ) )
            #time_zone = pytz.timezone('Asia/Kolkata')
            st = st.replace(tzinfo=time_zone)
            stu = st.astimezone(pytz.utc)
            et = et.replace(tzinfo=time_zone)
            etu = et.astimezone(pytz.utc)
            curren_time = timezone.now()
            #if curren_time >= st and curren_time <= et:
                #print 'True'
            #else:
                #print 'False'

            Configuration(task_type = tt, country = c, user_name = un, start_time = st, end_time = et, start_time_utc = stu, end_time_utc = etu, timezone = request.session['django_timezone']).save()
            #form.save()
            # redirect to a new URL:
            context = {'task_list': Configuration.objects.all(), 'timezones': pytz.common_timezones}
            return render(request, 'task/task.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, 'task/task_entry.html', {'form': form})

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        print "django_timezone set to ", request.session['django_timezone']
        return redirect('/task')
    else:
        return render(request, 'task/timezones.html', {'timezones': pytz.common_timezones})
