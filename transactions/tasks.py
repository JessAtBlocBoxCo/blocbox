# http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
from celery import Celery
from django.conf import settings
from watch_packages import main as watch_packages_task
app = Celery()
#app = Celery('tasks', broker=BROKER_URL)

@app.task
def add(x, y):  return x + y

@app.ask
def watch_packages():
    watch_packages_task()
    

if __name__ == '__main__':
    app.worker_main()