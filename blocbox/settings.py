"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.abspath(os.path.dirname(__name__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8ZYkjiMjzIYN2C5u3XkfPNC7xHYpREXYoIoBTlRYacvC52P43L'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'transactions',
    'south',   
    'djcelery',
    'datasci',
    'password_reset',
    'django_messages',
    'dateutil',
    'schedule',
    'calendar_homebrew',
    'connections',
    'billing',
    'paypal.standard.ipn',
		'testing',
)

#import celery and set it up
import djcelery
djcelery.setup_loader()

#set the broker url
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_IMPORTS = ['transactions.tasks']
#CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
    
#SET CELERY TIMEZONE AND SCHEDULE TASKS
CELERY_TIMEZONE = "US/Eastern"
from datetime import timedelta
CELERYBEAT_SCHEDULE = {
    'watch_packages_every_30_minutes': {
        'task': 'tasks.watch_packages',
        'schedule': timedelta(minutes=30),
    },
    'test_celery_beat_every_30_seconds': {
    	  'task': 'tasks.test_celery_beat',
    	  'schedule': timedelta(seconds=45),
    	  'args': (1,2,170)
    }
}   

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blocbox.urls'

WSGI_APPLICATION = 'blocbox.wsgi.application'

#USER AUTHENTICATION
AUTH_USER_MODEL = 'core.UserInfo'

AUTHENTICATION_BACKENDS = ('core.backends.EmailAuthBackEnd', 'django.contrib.auth.backends.ModelBackend',)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'OgdDdrmVUF',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    'home/django/blocbox/blocbox/static',
    'home/django/blocbox/bower_components/bootstrap/dist',
)

#Email Settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'admin@blocbox.co'
EMAIL_HOST_PASSWORD = '123GoodHood'
DEFAULT_FROM_EMAIL = 'admin@blocbox.co'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #this is defeault

#admins for error reporting
ADMINS = ('BlocBox Admin', 'admin@blocbox.co')


#template processors for the schedule app
TEMPLATE_CONTEXT_PROCESSORS = {
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth'
}

#Billing: Edit Settings.py,  from http://django-merchant.readthedocs.org/en/latest/overview.html#overview
# Authorize.Net settings
AUTHORIZE_LOGIN_ID = "..."
AUTHORIZE_TRANSACTION_KEY = "..."

# PayPal settings
PAYPAL_TEST = True
PAYPAL_WPP_USER = "..."
PAYPAL_WPP_PASSWORD = "..."
PAYPAL_WPP_SIGNATURE = "..."

#NEED TO UPDATE PAYPALE RECEIVER EMAIL - SO CORP ACCOUNT
PAYPAL_RECEIVER_EMAIL = "admin@blocbox.co"
PAYPAL_BUSINESS = "Blocbox"

#DEFINE THE AFTERSHIP API KEY
AFTERSHIP_API_KEY = '801e84c7-bae1-4afb-b294-51ca02a63d02'
AFTERSHIP_API_KEY_DEFAULT = '488caf4b-e7aa-4634-928b-2df5de94af9f'


#MEDIA_ROOT  FOR USER UPLOADED PICTURES AND POTENTIALLY OTHER FILES
#basedir is blocbox/blocbox. Note: needs to be 'writable' -- can't use static because thats not writable
#needs to be an absolute filepath e.g., "/var/www/example.com/media/"
MEDIA_ROOT = '/home/django/blocbox/blocbox/static/user_uploads/'
#MEDIA_URL is the base public url of that dir (not sure how different)
MEDIA_URL = '/static/user_uploads/'