# http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
from celery import Celery
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
#app = Celery()
#app = Celery('tasks', broker=BROKER_URL)
app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

@app.task
def add(x, y):  return x + y

from watch_packages import main as watch_packages_task
def watch_packages():
	  task = watch_packages_task()
	  #return HttpResponse(task)
	  return task   

from watch_packages import test_celery_beat
def test_schedule(enduserid, hostid, transid):
    return test_celery_beat(enduserid, hostid, transid)



if __name__ == '__main__':
    app.worker_main()