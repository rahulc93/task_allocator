# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(verbose_name=b'Start time for task')),
                ('end_time', models.DateTimeField(verbose_name=b'End time for task')),
                ('start_time_utc', models.DateTimeField(verbose_name=b'Start time for task in UTC')),
                ('end_time_utc', models.DateTimeField(verbose_name=b'End time for task in UTC')),
            ],
        ),
    ]
