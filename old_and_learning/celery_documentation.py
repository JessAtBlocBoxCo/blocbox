
#CELERY STUFF REMOVED FROM SETTINGS FILE
#set the broker url
#BROKER_URL = "amqp://jess:goodhood@localhost:5672/blocbox"
BROKER_URL = 'django://'
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
#CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI="postgresql://django:OgdDdrmVUF@localhost/django" 
 
#TRY CELERY IMPORTS
CELERY_IMPORTS = ['tasks']

#SET CELERY TIMEZONE AND SCHEDULE TASKS
CELERY_TIMEZONE = "US/Eastern"
from datetime import timedelta
CELERYBEAT_SCHEDULE = {

		'watch_packages_every_30_minutes': {
        'task': 'tasks.watch_packages',
        'schedule': timedelta(minutes=30),
    },
       'add_every_30_minutes': {
        'task': 'tasks.add',
        'schedule': timedelta(minutes=30),
        'args': (10,10) 
    },
}   

#TO FORCE IT TO RUN

#REMOVIMG CELERY
$ packages #go to packages dir
$ rm - r celery; rm -r djcelery #removing the packages
- remove djcelery from list of installed INSTALLED_APPS
- remove this line from blocbox/__init__.py:  from celeryconf import app as celery_app
-remove these lines form botton of settings file:
#import celery and set it up - should be at very bottom of settings file
#import djcelery
#djcelery.setup_loader()


#TASK SETS
1. core/usertasks.py -- these are tasks to updat ethe user model mostly
	CALL WITH - e.g., python; from core import usertasks; usertasks.get_zipcodes_nearby(2)
2. transactions/watchpackages.py -- key one - the function we're intersted in is "main"
	CALL MAIN WITH python; from transactions import watch_packages; watch_packages.main()

#WHERE I TELL CELERY WHAT TASKS TO RUN:
	blocbox/blocbox/settings.py - CELERYBEAT_SCHEDULE

#CHECK VERSION OF CELERYT
celery --VERSION #3.1.17 -- the newest is 3.1.17
#UPGRADING CELERYT
pip install -U celery

#START THE CELERY BEAT
$ celery -A blocbox beat #START THE SCHEDULER, I THINK THIS MIGHT BE THE SAME AS $celerybeat
#START NEW TERIMANL;start a worker in another terminal
python manage.py celery worker --loglevel=INFO

#runnign as daemon - i created thes tthree configures - THIS STARTS THE SCHEDULER, 
#but it doesn't actually start a worker
$ su jess #NEED TO RUN AS JESS
$ cd /etc/default
$ celeryd  #/etc/default/celeryd


#STOPPING IT
/etc/init.d/celerybeat stop #stop it
/etc/init.d/celeryd stop

#CHECK IF ITS RUNNING
/run/celery/beat.pid/
/var/run/celery/beat.pid/
/var/log/celery/beat.log/
/var/log/celery/w1.log/

#DEALING WITH PIDBOX IN USE ISSUE




#RUNNING CELERBYEAT AND WORKER AS DEAMON - THESE DO NOT APPEAR TO EXIT





/etc/default/celerybeat #but dont need this - just combine with celeryd
/etc/conf.d/celery

/etc/init.d/celeryd start
/etc/init.d/celerybeat start #start it
/etc/init.d/celerybeat stop #stop it
/etc/init.d/celeryd stop
#STOPPING IT
/etc/init.d/celerybeat stop #stop it


#PSLQ
tables: task state (on admin) = celery_taskmeta on the PSQL DJANGO back end
#I GOT A FLOOD OF TASKS - HOW TO DELETE HELLA TASKS FROM THAT TASK_STATES EMAIL
django; DELETE FROM celery_taskmeta WHERE id>6000; #etc... #result is 20 for add task

#WHERE AM I DESIGNING THEA DMIN PANEL FOR DJCELERY - THOSE TABLES?

#TO RUN THE SCHEDULER IN BACKGROUND
#ON THE ADMIN PANEL
task states is the importantone

#url
https://pypi.python.org/pypi/django-celery
	
#install it
$ pip install django-celery
--- this installed at: /usr/local/lib/python2.7/dist-packages/djcelery

#ADD TO SETTINGS.PY
INSTALLED_APPS += ("djcelery", )

CELERY_IMPORTS = ['transactions.tasks']
import djcelery
djcelery.setup_loader()

#celery user manual url
http://docs.celeryproject.org/en/latest/
	
	
#note: everythign works the same as the user manual but have to run it throug manage.py

Program	Replace with
celery	python manage.py celery
celery worker	python manage.py celery worker
celery beat	python manage.py celery beat
celery ...	python manage.py celery ...


#install the necessary tables
$ python manage.py migrate djcelery

#getting started with django - create celery.py
http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
	
#install a broker - rabbitmq
http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#broker-rabbitmq
	
#install it
$ sudo apt-get install rabbitmq-server
#When the command completes the broker is already running in the 
#background, ready to move messages for you: Starting rabbitmq-server: SUCCESS.


#configure the results backendin the tasks.py it looks like i want
app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')


#call the task again but with AsyncResult instance
$ result = add.delay(4,4)

#the ready() method returns wehther the task has finished processing
$ result.ready()
False

#you can wait for resut to compelte - but rarely used b/c it turns asynchornis into synrhous
$ result.get(timeout=1)


#SCHEDULING TATS

http://celery.readthedocs.org/en/latest/userguide/periodic-tasks.html



#ABOUT CELERY WORKERS VERSUS SCHEDLER

#to execute you need to start a worker
#STARTING THE WORKER PROCESS
In a production environment you will want to run the worker in the background as a daemon - 
see Running the worker as a daemon - but for testing and development it is useful to be able to start a worker instance by using the celery worker manage command, much as you would use Django’s runserver:

$ celery -A blocbox worker -l info  #thats an "L" lowercase not a 1




#i am getting the response
"""Running a worker with superuser privileges when the worker accepts messages serialized with pickle is a very bad idea!
If you really want to continue then you have to set the C_FORCE_ROOT environment variable (but please think about this before you do).
"""
#For a complete listing of the command-line options available, use the help command:
$ celery help

#stop celery worker

	

#STARTING THE SCHEDULERTo start the celery beat service:
$ celery -A blocbox beat

#start the cel;erybeat service
$ celerybeat

#You can also start embed beat inside the worker by enabling workers -B option, 
#this is convenient if you will never run more than one worker node, 
#but it’s not commonly used and for that reason is not recommended for production use:
$ celery -A blocbox worker -B

#Beat needs to store the last run times of the tasks in a local database file (named celerybeat-schedule by default), 
#so it needs access to write in the current directory, 
#or alternatively you can specify a custom location for this file:
$ celery -A blocbox beat -s /home/celery/var/run/celerybeat-schedule # - note i had to create this dir structure



#stop it from executing
^C??

#verify rabbitmq is working
sudo service rabbitmq-server status


#start logging
$ python manage.py celery worker -E
$ python manage.py celerycam


#different advice
http://stackoverflow.com/questions/10660202/how-do-i-set-a-backend-for-django-celery-i-set-celery-result-backend-but-it-is
$ python manage.py celeryd -E -B --loglevel=info #gettin error tasks not registered
#getting error: received UNREGISTERED TASKS

#open anaother termainal
$ .manage.py celerycam


#NEW APPROACH http://www.apreche.net/complete-single-server-django-stack-tutorial/
#first - get rabbit username and password
#when you install rabbitMQ you have to create  suer and grand permission on a virtual host
$ sudo apt-get install rabbitmq-server
$ sudo rabbitmqctl add_user jess goodhood #also added john
$ sudo rabbitmqctl add_vhost <RABBIT_VHOST> #can pick whatever vhost name you want - usually use app
$ sudo rabbitmqctl set_permissions -p <RABBIT_VHOST> jess ".*" ".*" ".*"
#using app..
$ sudo rabbitmqctl add_vhost blocbox #can pick whatever vhost name you want - usually use app
$ sudo rabbitmqctl set_permissions -p blocbox jess ".*" ".*" ".*"

#now go to celery
$ pip install django-celery
#edit settings
INSTALLED_APPS = 'djcelery'
BROKER_URL = "amqp://jess:goodhood@localhost:5672/blocbox"
CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI="postgresql://django:OgdDdrmVUF@localhost/django" #"postgresql://<DB_USER>:<DB_PASSWORD>@localhost/<DB_NAME>"

#PUT THESE AT VERY BOTTOM of settings.py
import djcelery
djcelery.setup_loader()

#getting error that no sqlalchemy - need to isntall
pip install SQLAlchemy

#now test celry with beat and event
$ ./manage.py celeryd -B -E
#start celery normally
python manage.py celeryd

#its possible it has to be run with manage.py celeryd rather than celeryd
#getting a DBAcess issue - probably because i dont hav write permissions
see: http://stackoverflow.com/questions/26756166/django-celery-beat-dbaccesserror
# instead go to place wher ei have write acces
python manage.py celeryd -B -E /home/django/blocbox/celerylogs


#documentign periodic tasks on django-celery
http://www.marinamele.com/2014/02/how-to-install-celery-on-django-and.html
	
#how to run periodoc task?
$ sudo rabbitmq-server -detached #1. start rbbitMQ server:	
$ python manage.py celery -verbosity=2 -loglevel=DEBUG #2. start a celery worker


#start a worker
python manage.py celery worker --loglevel=INFO


#SO IT WORKS WHEN I DO THE BEAT AND THEN START WORKER - EG.,
$ celery -A blocbox beat #and then stop it
$ python manage.py celery worker --loglevel=INFO #then when i do this later, the others send
#maybe add -b -e
$ python manage.py celery worker -B -E -loglevel=INFO
#note the B caues it to run the beats
#as if they were stored and then executed
$ celery -A blocbox worker -l info #antehr way to call the oworker

#can do this in two separate windows

#YES - THE WOREKR AND SCHEDULER ARE SEPARET - HAVE TO RUNT HE WORKER AND THE SCHEDULER

#YOU CAN START THEN BOTH BUT THIS ISN'T OFTEN USED FOR PRODUCTION?
$ celery -A blocbox worker -B


 

#django database

http://docs.celeryproject.org/en/3.0/getting-started/brokers/django.html#broker-django

BROKER_URL = 'django://'
INSTALLED_APPS = ('kombu.transport.django', )


#delete thte tables and recreate them
celery_taskmeta
celery_tasksetmeta
djcelery_crontabschedule
djcelery_intervalschedule CASCADE
djcelery_periodictask
djcelery_periodictasks
djcelery_taskstate
djcelery_workerstate

DROP TABLE celery_taskmeta;
DELETE FROM south_migrationhistory WHERE APP_NAME='DJCELERY'; 

#normaly staritn ig up
python manage.py celerycam
python manage.py celery worker -E --loglevel=INFO

#to admin view the celery_taskmeta table, fields: id, task_id, status, result, date_done traceback, hidden, meta

#TO VIEW ALL PROCESSES IN LINUX
$ ps aux | less
#delme: need to kill 

#RUNNIGN WORKER AS DAEMON (background)
http://celery.readthedocs.org/en/latest/tutorials/daemonizing.html#daemonizing
#get the init files here:

https://github.com/celery/celery/blob/3.1/extra/generic-init.d/celeryd
#documentaton on generic init scripts: 
http://docs.celeryproject.org/en/latest/tutorials/daemonizing.html#generic-init-scripts

#runnign as daemon - i created thes tthree configures
/etc/default/celeryd
/etc/default/celerybeat #but dont need this - just combine with celeryd
/etc/conf.d/celery

#and made these dirs
/var/log/celery
var/run/celery

#start celerybeat daemonize - need to also start the regular celer
/etc/init.d/celeryd_d start

/etc/init.d/celerybeat_d start #start it
/etc/init.d/celerybeat_d stop #stop it

