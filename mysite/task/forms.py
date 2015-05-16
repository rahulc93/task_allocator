from django import forms

class TaskForm(forms.Form):
    task_type = forms.CharField( label = 'Task Type', max_length = 100 )
    user_name = forms.CharField( label = 'User name', max_length = 100 )
    country = forms.CharField( label = 'Country', max_length = 100 )
    start_time = forms.DateTimeField( label = 'Start Time (Local)' )
    end_time = forms.DateTimeField( label = 'End Time (Local)' )

