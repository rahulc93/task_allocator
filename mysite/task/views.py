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
            user_name = form.cleaned_data['user_name']
            print "User Name entered: ", user_name
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, 'task/task_entry.html', {'form': form})
