#------------------------------
#Django app installed at: '/usr/lib/python2.7/dist-packages/django/contrib/admin/static/admin
#to print the version:
$ python -c "import django; print(django.get_version())" #this prints 1.6.5
#print source files - from python command line (enter python) with:
import sys 
sys.path = sys.path[1:] 
import django 
print(django.__path__)
quit()

#Enter into python command
$ python

#------------------------------
#things to change if you rename project
/etc/init/gunicorn.conf
/etc/nginx/sites-enabled/django:
	
#------------------------------
#Reload changes
service gunicorn restart

#---------------
#if change nginx restart changes
sudo service nginx restart

#---------------------------------
#NEW IP

#-------------------------------
# Access database
psql django
\dt #show tables
\d #show columns

"""----------------------------------------------
#BB DJANGO - THE ONE-CLICK DNAGO INSTALL
#Admin Site: http://162.243.57.182:9000/admin/; username: jyeats; password=goodhood
#Django Tutorial (mysite = home/django/django_project)
#Django version: 1.6.5    
#Python version: 2.7.6

#ROOT PASSWORD: goodhood

"""

#-----
#To make the CSS load on the admin page, added this to /opt/myenv/myproject/myproject/urls.py
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )


#--------------------------------------------------------------------

#INDENTATINO MATTERS - USE 4 SPACES RATHER THAN A TAB
#IP: 104.131.244.240
#--------------------------------------

"""Create a root password so you can su (switch users)"""
passwd
goodhood

"""and to give root acces sto djano database"""

"""to add an alias to /home/django/blocbox"""
nano ~/.bashrc
"""NEED TO EDIT ROOT PASSWORD SO I'M NOT PROMPTED FOR A PASSWORD
It's necessary need to edit the server's SSHd configuration 
/etc/ssh/sshd_config and update the following line to now read:
"""
PermitRootLogin without-password

"""First  install django, postgre, nginx, gunicorn manually """

#first, check for updates and upgrades
sudo apt-get update
sudo apt-get upgrade

"""STEP TWO: Install and Create VirtualEnv"""
#virtualenv is a tool to create isolate python environents. Creates a copy of python in whicever directory you ran the comand in,
#	placing it in a folder named venv
sudo apt-get install python-virtualenv


#Create virtulevt so we can install django and python packages with it
sudo virtualenv /opt/myenv #this creates a new /opt directory where the virtualenv will live,
	#replace /opt/myenv with the path to where you want your virtualenv installed

"""STEP THREE: INSTALL DJANGO"""
#NFirst -  activate virtualEnv so that we install python packages they install to our virtualenv
source /opt/myenv/bin/activate

#next, install django - using pip pythong package
pip install django


"Step 4: install postgreSQL"
#deactivate virtualenv
deactivate
sudo apt-get install libpq-dev python-dev #dependencies for django to work with postgre
sudo apt-get install postgresql postgresql-contrib #install postgre

su
"""install NGINX- a fast and lightweight web server, use it to serve up 
	static files for our Django app"""
sudo apt-get install nginx
#you still need to start it!

"""Step 6: install Gunicorn: A python WSGI HTTP server, 
since its python, we need to adtivate virtualent o instal"""
#activate virtualenv
source /opt/myenv/bin/activate
#install gunicorn
pip install gunicorn



"""Step 7: configure postgreSQL"""
sudo su - postgres #i think this activate it'
createdb mydb #create a database

createuser -P 
#EDIT - THE COMMAND THAT WORKED FOR ME WAS:
createuser jess -P #and then i entered a password

the password is goodhood but im not sure well setup...
#enter username
#enter password, and confirm
#for next two promts enter "n" and hit "enter - 

#activate the postgreSQL command line interace
psql
GRANT ALL PRIVILEGES ON DATABASE mydb TO jess;
\q #to quit postgresql

"""Step 8 : STart djangoF project
In order to go any further we need a Django project to test with. 
This will allow us to see if what we are doing is working or not. 
Change directories into the directory of your virtualenv (in my case /opt/myenv) like so:"""

#NOTE - change users back to root with "su"

cd /opt/myenv

# Now make sure your virtualenv is active. If you're unsure then just run the following command to ensure you're activated:

source /opt/myenv/bin/activate

#With your virtualenv now active, run the following command to start a new Django project:

django-admin.py startproject myproject

#You should see a new directory called "myproject" inside your virtualenv directory. 
#This is where our new Django project files live.

"""In order for Django to be able to talk to our database we need to install a backend for 
PostgreSQL. Make sure your virtualenv is active and run the following command in order to do this:"""

pip install psycopg2

"""Change directories into the new "myproject" directory and then into it's subdirectory
 which is also called "myproject" like this:"""

cd /opt/myenv/myproject/myproject

# Edit the settings.py file with your editor of choice:

nano settings.py

Find the database settings and edit them to look like this:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'mydb',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'jess',
            'PASSWORD': 'goodhood',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }

#Save and exit the file. Now move up one directory so your in your main Django project directory (/opt/myenv/myproject).

cd /opt/myenv/myproject

#Activate your virtualenv if you haven't already with the following command:

source /opt/myenv/bin/activate

#With your virtualenv active, run the cmd so that Django can add it's initial config and other tables to your database:
python manage.py syncdb

"""CREATE A SUPERUSER
You should see some output describing what tables were installed, followed by a
 prompt asking if you want to create a superuser. This is optional and depends on if you will be using Django's auth system or the Django admin
"""
superuser:jess; passwood: goodhood


"""Step Nine: Configure Gunicorn
Gunicorn configuration is very specific to your applications needs. 
I will briefly go over running Gunicorn here with some different settings.

First lets just go over running Gunicorn with default settings. 
Here is the command to just run default Gunicorn:"""

#gunicorn_django --bind yourdomainorip.com:8001
gunicorn_django --bind 104.131.244.240:8001

"""
Be sure to replace "yourdomainorip.com" with your domain, or the IP address of your VPS if you prefer. 
Now go to your web browser and visit yourdomainorip.com:8001 and see what you get. 
You should get the Django welcome screen.

If you look closely at the output from the above command however, 
you will notice only one Gunicorn worker booted. 
What if you are launching a large-scale application on a large VPS? 
Have no fear! All we need to do is modify the command a bit like so:"""

#gunicorn_django --workers=3 --bind yourdomainorip.com:8001
gunicorn_django --workers=3 --bind 104.131.244.240:8001
#Note - i'm getting an error WARNING - THIS COMMAND IS DEPRECATED, INTERNET SAYS USE:
gunicorn --bind 104.131.244.240:8001 myproject.wsgi:application
	
"""Now you will notice that 3 workers were booted instead of just 1 worker. 
You can change this number to whatever suits your needs."""
#ERROR - THAT IDN'T WORK

"""RUNNING AS ROOT VERSUS ANOTHER USERS
Since we ran the command to start Gunicorn as root, Gunicorn is now running as root. 
What if you don't want that? Again, we can alter the command above slightly to accomodate:"""

gunicorn_django --workers=3 --user=nobody --bind yourdomainorip.com:8001

"""
If you want to set more options for Gunicorn, 
then it is best to set up a config file that you can call when running Gunicorn.
 This will result in a much shorter and easier to read/configure Gunicorn command.

You can place the configuration file for gunicorn anywhere you would like. 
For simplicity, we will place it in our virtualenv directory. Navigate to the directory of your virtualenv like so:"""

cd /opt/myenv

#Now open your config file with your preferred editor (nano is used in the example below):

sudo nano gunicorn_config.py

Add the following contents to the file:

    command = '/opt/myenv/bin/gunicorn'
    pythonpath = '/opt/myenv/myproject'
    bind = '104.131.244.240:8001'
    workers = 3
  #  user = nobody #comenting that out - just running as root

#Save and exit the file. 
#What these options do is to set the path to the gunicorn binary, 
#add your project directory to your Python path, 
#set the domain and port to bind Gunicorn to, 
#set the number of gunicorn workers and set the user Gunicorn will run as.

#In order to run the server, this time we need a bit longer command. 
#Enter the following command into your prompt:

/opt/myenv/bin/gunicorn -c /opt/myenv/gunicorn_config.py myproject.wsgi

# You will notice that in the above command we pass the "-c" flag. 
#This tells gunicorn that we have a config file we want to use, which we pass in just after the "-c" flag. 
#Lastly, we pass in a Python dotted notation reference to our WSGI file so that Gunicorn knows where our WSGI file is.

#Running Gunicorn this way requires that you either run Gunicorn in its own screen session (if you're familiar with using screen), 
#or that you background the process by hitting "ctrl + z" and then typing "bg" and "enter" all right after running the Gunicorn command. 
#This will background the process so it continues running even after your current session is closed. 
#This also poses the problem of needing to manually start or restart Gunicorn should your VPS gets rebooted or were it to crash for some reason. 
#To solve this problem, most people use supervisord to manage Gunicorn and start/restart it as needed. 
#Installing and configuring supervisord has been covered in another article which can be found here.
https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps 

#to stop gunicorn - find the process
ps ax|grep gunicorn
kill [process]
	

"""STEP 10:Configure NGINX"""

sudo service nginx start

"""Since we are only setting NGINX to handle static files we need to 
first decide where our static files will be stored. 
Open your settings.py file for your Django project and edit the 
STATIC_ROOT line to look like this:"""

STATIC_ROOT = "/opt/myenv/static/"

"""This path can be wherever you would like. 
But for cleanliness, I typically put it just outside my Django project folder, but inside my virtualenv directory."""

"""Now that you've set up where your static files will be located, let's configure NGINX to handle those files. 
Open up a new NGINX config file with the following command (you may replace "nano" with your editor of choice):"""

sudo nano /etc/nginx/sites-available/myproject

#You can name the file whatever you would like, but the standard is typically to name it something related to the site that you are configuring. Now add the following to the file:

    server {
        server_name 104.131.244.240;

        access_log off;

        location /static/ {
            alias /opt/myenv/static/;
        }

        location / {
                proxy_pass http://104.131.244.240:8001;
                proxy_set_header X-Forwarded-Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
        }
    }
Save and exit the file. The above configuration has set NGINX to serve anything requested at yourdomainorip.com/static/ from the static directory we set for our Django project. Anything requested at yourdomainorip.com will proxy to localhost on port 8001, which is where we told Gunicorn to run. The other lines ensure that the hostname and IP address of the request get passed on to Gunicorn. Without this, the IP address of every request becomes 127.0.0.1 and the hostname is just your VPS hostname.

#Now we need to set up a symbolic link in the /etc/nginx/sites-enabled directory that points to this configuration file. That is how NGINX knows this site is active. Change directories to /etc/nginx/sites-enabled like this:
cd /etc/nginx/sites-enabled

#Once there, run this command:
sudo ln -s ../sites-available/myproject

"""This will create the symbolic link we need so that NGINX knows to honor our new configuration file for our site.
Additionally, remove the default nginx server block:"""
sudo rm default

#We need to restart NGINX though so that it knows to look for our changes. To do this run the following:
sudo service nginx restart




#update the admin css page 
#To make the CSS load on the admin page, added this to /home/django/django_project/django_project/urls.py
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )









#----------------------------------------------
#how to install missing CSS on admin page
#-------------------------------------------------------------

#Understanding the URLs statement in /home/django/blocbox/blocbox/urls.py
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

#Restart guninx
service gunicorn restart

#where is the admin url/page located?


#Creaqte superuser/passowrds
python manage.py createsuperuser --username=jyeats --email=jessica.yeats@gmail.com

# single line comment 
" " " this is a multiline comment   
which spawns many lines 
" " "

#check if you have django installed: 
$ python -c "import django; print(django.get_version())" #this prints 1.6.5

#change into the outer mysite directory (home/django/django_project) 
#start the django development server with 
python manage.py runserver
"""output:
Django version 1.6.5, using settings 'django_project.settings'
Starting development server at http://127.0.0.1:8000/
the 8000 port - this is local port"""
#note: http://127.0.0.1:8000/ actually means http://162.243.57.182:9000/
#Guncorn runs on 9000 port (not 8000) and 127.0.0.1 = localhost = IP address for machine 

"""For DigitalOcean, The Django project is served by Gunicorn which 
listens on port 9000 and is proxied by Nginx which listens on port 80.
NGINX configuration is located at /etc/nginx/sites-enabled/django:
	points to static files (like media, images, url management): /home/django/django_project/django_project)
	If you rename the project folder, remember to change the path to your static files in this file"""

#had to edit the location alias
#NOT TRUE - THEY ARE ACTUALLY FOUND HERE: '/usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/admin

#Restart Nginx with cmd: 
sudo /etc/init.d/nginx restart

"""GUNICORN is started on boot by an Upstart script located at /etc/init/gunicorn.conf
 	if  you rename the project folder, remember to update the name and pythonpath in this file
	upstart script also sources a config file in etc/gunincorn.d/gunicorn.py that sets the number of worker processes"""
#DJANGO: project located in /home/django/django_project
	#RESTART (e.g., after making chnages) with 
service gunicorn restart

#however, while running, it can be annoying to restart with changes
#you can use Django's build in development server which automatically detects changes
service gunicorn stop
python manage.py runserver localhost:9000
"""output:
Django version 1.6.5, using settings 'django_project.settings'
Starting development server at http://localhost:9000/ """

#--------------------------------------------------------------------------
#Database Setup
#uses SQLite, which is included in Python
#--------------------------------------------------------------------------
"""edit mysite/settings.py - home/django/blocbox/blocbox/settings.py)
"""

#Database Configuration - using Postgre
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': '3xsRDPTuG1',
        'HOST': 'localhost',
        'PORT': '',
    }
}

#first - change timezone
TIME_ZONE = 'UTC'
#to
TIME_ZONE = 'US/Pacific'

#Note the installed apps at the top of the settings.py page


"""some of these applications make use of at least one database table, 
so we need to create the tables in the database before we can use them w/cmd"""
python manage.py syncdb
"""the syncdb cmd looks at the INSTALLED_APPS settings and creates any
necessay database tables according to the database settings in your mysite/settings.py file
you'll see a message for each database table it creates, and you'll get a prompt
asking you if you'dl ike to create a superuser account for the authentication"""

#--------------------------------------------------------------------
#Create the first app (cd to directory with manage.py)
#https://docs.djangoproject.com/en/1.6/intro/tutorial01/
#--------------------------------------------------------------------
python manage.py startapp polls 
	#creates dir polls, has: _init_.py admin.py models.py tests.py views.py
	#this dir will hold the polls app
	#Note: a model is the single, definitely source of data about your data
	#python follows the DRY (dont repeat yourself) philosophy - define data model in one place and auto derive thingsfrom it

#next, edit the polls/models.py file (per the website)
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200) #a field instance, column name in db = question
    pub_date = models.DateTimeField('date published') #colujn name = pub_date

class Choice(models.Model):
    poll = models.ForeignKey(Poll) #Relationship is defined, each choice is relatd to a ingle Poll
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
"""what it means:
the program creates two models: poll and Choice
each model has a number of class vars,
each of which represents a databse field in the model
EAch fiel is represented by an instance of a Field class 
Some field classes have required arguments.
Charfield, e.g., requires that you give it a max_length
A field can also have various optional arguments
in this case, we've set the default value of votes to 0
"""

#Activating Models
"""Code above allos Django to 
1. create a database scheme (CREATE TABLE statements for this app);
2; Create a python database-access API for accessing Poll and Choice objects
"""
#First, we need to tell our project that polls app is installed
"""Philosophy: django apps are "poluggable" - you can use an app in multiple projects,
and you an distribute apps, because they dont have to be tied to a given Django installation
"""
#Edit the settings.py file again, change INSTALLED_APPS settings to include the string 'polls
INSTALLED_APPS = (
    'django.contrib.admin', #the admin site, you'll use it in part 2 of the tutoial
    'django.contrib.auth', #an authentication system
    'django.contrib.contenttypes', #a framework for content types
    'django.contrib.sessions', #a session framework
    'django.contrib.messages', #a messaging framework
    'django.contrib.staticfiles', #a framework for managing static files
    'polls', #just added
)

#Run the cmd:
python manage.py sql polls 

#Output:
BEGIN;
CREATE TABLE "polls_poll" (
    "id" serial NOT NULL PRIMARY KEY,
    "question" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
)
;
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "poll_id" integer NOT NULL REFERENCES "polls_poll" ("id") DEFERRABLE INITIALLY DEFERRED,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL
)
;


"""note:
1. table names automatially generated by combining name of app (polls) and lower case name of model (choice)
2. primary keys (IDs) are aed automtcilly
.."""

#Create run other cmds:
python manage.py validate #checks for errors in model
python manage.py sqlcustom polls #outputs custom SQL statements defined for app
python manage.py sqlclear polls #outputs necessary DROP TABLE statements for this app, according to which table exist
python manage.py sqlindexes polls #ouputs the CREATE INDEX statement for app
python manage.py sqall polls #a combination of all the SQL from the sql, sqlcustom ad sqlindexes commands

#Create the databases in your databe with cmd
python manage.py syncdb 
	#this ommand creates tables, initial data and indexes for any apps you've added since last time running cmd
	#created polls_poll and polls_choice tables
	#can be called whenever you like, only creates the tables that dont already exist
	
	
#Playing with the API, by invoking the Python shell
python manage.py shell
"""Note: you dont have to use manage.py if you modify the env vars to inclue manage.py, but whatever"""

#once you're in the shell, explore the database API:

>>> from polls.models import Poll, Choice   # Import the model classes we just wrote.


>>> Poll.objects.all() # REutnrs []No polls are in the system yet.

# Create a new Poll questionp.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone #see tie with timezone.now()
>>> p = Poll(question="What's new?", pub_date=timezone.now())


# Save the object into the database. You have to call save() explicitly.
>>> p.save()

# CHECK THE ID WITH P.ID
>>> p.id #returns "1"

# Access database columns via Python attributes.
>>> p.question
"What's new?"
>>> p.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> p.question = "What's up?"
>>> p.save()

# objects.all() displays all the polls in the database.
>>> Poll.objects.all() #returns: [<Poll: Poll object>]

""" <Poll: Poll object> is, utterly, an unhelpful representation of this object. 
Let’s fix that by editing the polls model (in the polls/models.py file) 
and adding a __unicode__() method to both Poll and Choice. :"""

from django.db import models

class Poll(models.Model):
    # ...
    def __unicode__(self):  #ADD THIS
        return self.question

class Choice(models.Model):
    # ...
    def __unicode__(self):  # ADD THIS
        return self.choice_text
 
#Save these changes and start a new pythong interactive shell with       
python manage.py shell

##when in the interactive shell,thype:
>>> from polls.models import Poll, Choice

# Make sure our __unicode__() addition worked.
>>> Poll.objects.all() #returns: [<Poll: What's up?>], whereas formerly returned "Poll: Poll object


# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Poll.objects.filter(id=1) #returns field with id=1 (p): Po[<Poll: What's up?>]
>>> Poll.objects.filter(question__startswith='What')#reutnrs [<Poll: What's up?>]
	#NOTE - there are two underscores btween 'question and 'startswith'
	
# Get the poll that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Poll.objects.get(pub_date__year=current_year) #Returns Poll: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Poll.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Poll matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a shortcut for primary-key exact lookups.
# The following is identical to Poll.objects.get(id=1).
>>> Poll.objects.get(pk=1) #Returns - Poll: What's up?>

# Make sure our custom method worked.
>>> p = Poll.objects.get(pk=1) #Defines variable p
>>> p.was_published_recently() #Returns 'True'

# Give the Poll a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a poll's choices) which can be accessed via the API.
>>> p = Poll.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> p.choice_set.all() #returns []

# Create three choices.
>>> p.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> p.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = p.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Poll objects.
>>> c.poll #returns: Poll: What's up?>

# And vice versa: Poll objects get access to Choice objects.
>>> p.choice_set.all()
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]
>>> p.choice_set.count() #returns '3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any poll whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(poll__pub_date__year=current_year)
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]

# Let's delete one of the choices. Use delete() for that.
>>> c = p.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()


