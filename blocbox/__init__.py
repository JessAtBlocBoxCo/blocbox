from __future__ import absolute_import
# This will make sure the app is always imported when Django starts so that shared_task will use this app.
# from: http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
from .__celery import app as celery_app