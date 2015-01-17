#This is blocbox.calendar_homeless.models.py
from django.db import models
import pytz
from django.contrib.contenttypes import generic
from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
import datetime
from schedule.utils import EventListManager
from django.utils import timezone
from django.conf import settings


	
	
#Define a conflicts model - conflicts populate the availability model?
class HostConflicts(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='host_conflict', blank=True, null=True) #this shows up as payer_id
    #date_from is the same as 'date' if its only one day
    date_from = models.DateField(null=True) #Remember, blank determines whether or not it can be blank on forms - null is whether required o model
    date_to = models.DateField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True) #when writing an view to take the cal data, make this automatically subtract date_from from date_to (+1 to capture today)
    allday = models.BooleanField("All Day?", default=False, blank=True)
    am = models.BooleanField("AM Conflict", default=False, blank=True)
    pm = models.BooleanField("PM Conflict", default=False, blank=True)
    time_from = models.TimeField("Time: From", blank=True, null=True)
    time_to = models.TimeField("Time: To", blank=True, null=True)
    datetime_added = models.DateTimeField(default=datetime.datetime.today, blank=True, null=True)
    date_added = models.DateField("Date Conflict Added by Host", default = datetime.date.today, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)   
   


#default daily schedule
class HostWeeklyDefaultSchedule(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='host_weeklyschedule', blank=True, null=True) 
    #Boolean fields for each day of week
    #Note that these days are defaulting true - have the user uncheck if not available
    monday_available = models.BooleanField("Mon", default=True, blank=True)
    tuesday_available = models.BooleanField("Tues", default=True, blank=True)
    wednesday_available = models.BooleanField("Weds", default=True, blank=True)
    thursday_available = models.BooleanField("Thur", default=True, blank=True)
    friday_available = models.BooleanField("Fri", default=True, blank=True)
    saturday_available = models.BooleanField("Sat", default=True, blank=True) 
    sunday_available = models.BooleanField("Sun", default=True, blank=True) 
    #Available times: default every day
    #If they only have one window, use window1
    default_time1_from = models.TimeField("Default Time Available: From (Window 1)", blank=True, null=True)
    default_time1_to   = models.TimeField("Default Time Available: To (Window 1)",   blank=True, null=True)
    default_time2_from = models.TimeField("Default Time Available: From (Window 2)", blank=True, null=True)
    default_time2_to   = models.TimeField("Default Time Available: To (Window 2)",   blank=True, null=True)   
    default_time3_from = models.TimeField("Default Time Available: From (Window 3)", blank=True, null=True)
    default_time3_to   = models.TimeField("Default Time Available: To (Window 3)",   blank=True, null=True)   
    default_time4_from = models.TimeField("Default Time Available: From (Window 4)", blank=True, null=True)
    default_time4_to   = models.TimeField("Default Time Available: To (Window 4)",   blank=True, null=True)  
    #Monday time available
    monday_time1_from = models.TimeField("Default Time Available: From (Window 1)", blank=True, null=True)
    monday_time1_to   = models.TimeField("Default Time Available: To (Window 1)",   blank=True, null=True)
    monday_time2_from = models.TimeField("Default Time Available: From (Window 2)", blank=True, null=True)
    monday_time2_to   = models.TimeField("Default Time Available: To (Window 2)",   blank=True, null=True)   
    monday_time3_from = models.TimeField("Default Time Available: From (Window 3)", blank=True, null=True)
    monday_time3_to   = models.TimeField("Default Time Available: To (Window 3)",   blank=True, null=True)   
    monday_time4_from = models.TimeField("Default Time Available: From (Window 4)", blank=True, null=True)
    monday_time4_to   = models.TimeField("Default Time Available: To (Window 4)",   blank=True, null=True)  
    #Tuesday time available
    tuesday_time1_from = models.TimeField("Default Time Available: From (Window 1)", blank=True, null=True)
    tuesday_time1_to = models.TimeField("Default Time Available: To (Window 1)", blank=True, null=True)
    tuesday_time2_from = models.TimeField("Default Time Available: From (Window 2)", blank=True, null=True)
    tuesday_time2_to = models.TimeField("Default Time Available: To (Window 2)", blank=True, null=True)   
    tuesday_time3_from = models.TimeField("Default Time Available: From (Window 3)", blank=True, null=True)
    tuesday_time3_to = models.TimeField("Default Time Available: To (Window 3)", blank=True, null=True)   
    tuesday_time4_from = models.TimeField("Default Time Available: From (Window 4)", blank=True, null=True)
    tuesday_time4_to = models.TimeField("Default Time Available: To (Window 4)", blank=True, null=True)  
    #Wednesday time available
    wednesday_time1_from = models.TimeField("Default Time Available: From (Window 1)", blank=True, null=True)
    wednesday_time1_to = models.TimeField("Default Time Available: To (Window 1)", blank=True, null=True)
    wednesday_time2_from = models.TimeField("Default Time Available: From (Window 2)", blank=True, null=True)
    wednesday_time2_to = models.TimeField("Default Time Available: To (Window 2)", blank=True, null=True)   
    wednesday_time3_from = models.TimeField("Default Time Available: From (Window 3)", blank=True, null=True)
    wednesday_time3_to = models.TimeField("Default Time Available: To (Window 3)", blank=True, null=True)   
    wednesday_time4_from = models.TimeField("Default Time Available: From (Window 4)", blank=True, null=True)
    wednesday_time4_to = models.TimeField("Default Time Available: To (Window 4)", blank=True, null=True)  
    #Thursday time available
    thursday_time1_from = models.TimeField("Default Time Available: From (Window 1)", blank=True, null=True)
    thursday_time1_to = models.TimeField("Default Time Available: To (Window 1)", blank=True, null=True)
    thursday_time2_from = models.TimeField("Default Time Available: From (Window 2)", blank=True, null=True)
    thursday_time2_to = models.TimeField("Default Time Available: To (Window 2)", blank=True, null=True)   
    thursday_time3_from = models.TimeField("Default Time Available: From (Window 3)", blank=True, null=True)
    thursday_time3_to = models.TimeField("Default Time Available: To (Window 3)", blank=True, null=True)   
    thursday_time4_from = models.TimeField("Default Time Available: From (Window 4)", blank=True, null=True)
    thursday_time4_to = models.TimeField("Default Time Available: To (Window 4)", blank=True, null=True)  
    #Friday time available
    friday_time1_from = models.TimeField("Default Time Available: From (Window 1)", blank=True, null=True)
    friday_time1_to = models.TimeField("Default Time Available: To (Window 1)", blank=True, null=True)
    friday_time2_from = models.TimeField("Default Time Available: From (Window 2)", blank=True, null=True)
    friday_time2_to = models.TimeField("Default Time Available: To (Window 2)", blank=True, null=True)   
    friday_time3_from = models.TimeField("Default Time Available: From (Window 3)", blank=True, null=True)
    friday_time3_to = models.TimeField("Default Time Available: To (Window 3)", blank=True, null=True)   
    friday_time4_from = models.TimeField("Default Time Available: From (Window 4)", blank=True, null=True)
    friday_time4_to = models.TimeField("Default Time Available: To (Window 4)", blank=True, null=True)  
    #Saturday time available
    saturday_time1_from = models.TimeField("Default Time Available: From (Window 1)", blank=True, null=True)
    saturday_time1_to = models.TimeField("Default Time Available: To (Window 1)", blank=True, null=True)
    saturday_time2_from = models.TimeField("Default Time Available: From (Window 2)", blank=True, null=True)
    saturday_time2_to = models.TimeField("Default Time Available: To (Window 2)", blank=True, null=True)   
    saturday_time3_from = models.TimeField("Default Time Available: From (Window 3)", blank=True, null=True)
    saturday_time3_to = models.TimeField("Default Time Available: To (Window 3)", blank=True, null=True)   
    saturday_time4_from = models.TimeField("Default Time Available: From (Window 4)", blank=True, null=True)
    saturday_time4_to = models.TimeField("Default Time Available: To (Window 4)", blank=True, null=True)  
    #Sunday time available
    sunday_time1_from = models.TimeField("Default Time Available: From (Window 1)", blank=True, null=True)
    sunday_time1_to = models.TimeField("Default Time Available: To (Window 1)", blank=True, null=True)
    sunday_time2_from = models.TimeField("Default Time Available: From (Window 2)", blank=True, null=True)
    sunday_time2_to = models.TimeField("Default Time Available: To (Window 2)", blank=True, null=True)   
    sunday_time3_from = models.TimeField("Default Time Available: From (Window 3)", blank=True, null=True)
    sunday_time3_to = models.TimeField("Default Time Available: To (Window 3)", blank=True, null=True)   
    sunday_time4_from = models.TimeField("Default Time Available: From (Window 4)", blank=True, null=True)
    sunday_time4_to = models.TimeField("Default Time Available: To (Window 4)", blank=True, null=True)  
    #Schedule Notes
    monday_note = models.CharField(max_length=200, blank=True, null=True)
    tuesday_note = models.CharField(max_length=200, blank=True, null=True)
    wednesday_note = models.CharField(max_length=200, blank=True, null=True)
    thursday_note = models.CharField(max_length=200, blank=True, null=True)
    friday_note = models.CharField(max_length=200, blank=True, null=True)
    saturday_note = models.CharField(max_length=200, blank=True, null=True)
    sunday_note = models.CharField(max_length=200, blank=True, null=True)  
    #Date schedule created
    date_schedule_created = models.DateField(default=datetime.date.today, blank=True, null=True)
    date_last_updated = models.DateTimeField(default=datetime.datetime.today, blank=True, null=True)
   