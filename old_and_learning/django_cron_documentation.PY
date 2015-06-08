http://django-cron.readthedocs.org/en/latest/installation.html
http://django-cron.readthedocs.org/en/latest/

#TO MAKE IT WORK HAVE TO EDIT CRONTABBL FILE
https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-on-a-vps
locatied at: CD /var/spool/cron/crontab
$ crontab -e #opens it up

#HOW TO SCHEDULE IT: THE COMMAND
python /home/django/blocbox/manage.py runcrons
#ADDED THE FOLLOWING
* * * * * /home/django/blocbox/manage.py runcrons #every minute
#HOW TO SCHEDULE PERIODICALY
12 * * * * #To run a command every 12th minute on the hour:
0,15,30,45 * * * * #You can also use different options for each placeholder. To run a command every 15 minutes:

#THE LOG OF THE TASKS
/var/log/crontab_runcrons.log

#CHECK IF CRON DAEMON IS RUNNING
$ ps -ax|grep cron
$ ps ax|grep cron


#CRON TASSKS
blocbox/transactions/cron.py -CALLS transactions/watch_packages.py
#RUN IT - this should run all the crons
$ python manage.py runcrons # all the crons will run if required.

#uninstsall then reinstall
$ sudo apt-get --purge autoremove django_cron

#installation
$ pip install django_cron

#ADD TO INSTALLED  APPS: 
'django_cron'

#MIGRATE IT
python manage.py migrate django_cron

#REMOVE FROM SOUTH
DELETE FROM south_migrationhistory WHERE app_name = 'transactions';

#TASK FILES

1. core/usertasks.py -- these are tasks to updat ethe user model mostly
	CALL WITH - e.g., python; from core import usertasks; usertasks.get_zipcodes_nearby(2)
2. transactions/watchpackages.py -- key one - the function we're intersted in is "main"
	CALL MAIN WITH python; from transactions import watch_packages; watch_packages.main()

#WHEN I TRY TO LOAD WATCHPACKAGES.PY FROM PYTHON SHELL I GET ERROR "models aren't loaded yet"
#stack overflow page: http://stackoverflow.com/questions/25537905/django-1-7-throws-django-core-exceptions-appregistrynotready-models-arent-load
# suggests revising wsgi.py file (blocbox/blocbox/wsgi.py):
#try adding this to top
import django
django.setup()


#NEED TO DROP THESE TABLES FROM SCHEULD
schedule_calendar CASCADE
schedule_calendarrelation CASCADE
schedule_event
schedule_eventrelation
schedule_occurence
schedule_rule


#LOOK IN NGINX ERROR LOG
/var/log/nginx/error.log
#SOMETHING GOT FUCKED UP - GATEWAY TIME OUT - HAD TO KILL ALL PROCESSES
$ kill -15 -1

#BUT NOW THE SITE IS DOWN

#ADJUST NGINX CONFIG ?
/etc/nginx/
