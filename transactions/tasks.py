# http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
from celery import Celery
from django.conf import settings

app = Celery()
#app = Celery('tasks', broker=BROKER_URL)

@app.task
def add(x, y):  return x + y


if __name__ == '__main__':
    app.worker_main()