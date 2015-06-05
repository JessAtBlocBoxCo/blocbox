from __future__ import absolute_import

import os
import celery

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blocbox.settings')

app = Celery('blocbox')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#this allows celery to autodiscover tasks that follow the app/tasks.py convention


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))