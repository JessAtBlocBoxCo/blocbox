# http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
from celery import Celery
from celery import task
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from watch_packages import main as watch_packages_task
from watch_packages import test_celery_beat
#app = Celery()
#app = Celery('tasks', broker=BROKER_URL)
#app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost:5672//')
app = Celery('tasks', backend='amqp', broker="amqp://jess:goodhood@localhost:5672/blocbox")

@app.task
def add(x, y):  return x + y


@app.task
def watch_packages():
	  task = watch_packages_task()
	  #return HttpResponse(task)
	  return task   

@app.task
def test_schedule(enduserid, hostid, transid):
    return test_celery_beat(enduserid, hostid, transid)



if __name__ == '__main__':
    app.worker_main()