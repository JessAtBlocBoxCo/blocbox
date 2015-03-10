# http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
from celery import Celery
from celery import task
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from transactions.watch_packages import main as watch_packages_task
from transactions.watch_packages import test_celery_beat
from core.usertasks import get_zipcodes_nearby, add_zipcodes_nearby, delete_zipcodes_nearby, add_zipcodes_nearby_all, set_default_mileradius_task, set_mileradius_user_task
from celeryconf import app
#app = Celery('blocbox')
#app = Celery('tasks', broker=BROKER_URL)
#app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost:5672//')
#app = Celery('tasks', backend='amqp', broker="amqp://jess:goodhood@localhost:5672/blocbox")

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


@app.task
def get_zips_nearby(userid):
    return get_zipcodes_nearby(userid, mileradius)

@app.task
def add_zips_nearby(userid, mileradius):
   return add_zipcodes_nearby(userid, mileradius)
 
@app.task
def delete_zips_nearby():
    return delete_zipcodes_nearby()
    
@app.task
def add_zips_nearby_all(mileradius):
    return add_zipcodes_nearby_all(mileradius)

@app.task 
def set_default_mileradius(mileradius):
    return set_default_mileradius_task(mileradius)

@app.task
def set_mileradius_user(userid, mileradius):
    return set_mileradius_user_task(userid, mileradius)


if __name__ == '__main__':
    app.worker_main()