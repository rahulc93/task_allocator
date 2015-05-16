from django.db import models

# Create your models here.

class Configuration(models.Model):
    task_type = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    timezone = models.CharField(max_length=200)
    local_time_zone = models.CharField(max_length=200)
    start_time = models.DateTimeField('Start time for task')
    end_time = models.DateTimeField('End time for task')
    start_time_utc = models.DateTimeField('Start time for task in UTC')
    end_time_utc = models.DateTimeField('End time for task in UTC')
    #status = models.DateTimeField('Status of the Task')
