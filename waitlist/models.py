from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings 

class Waitlist(AbstractBaseUser): #standard fields defined below
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField('First Name',max_length=100, blank=True)    
    zipcode = models.CharField(max_length =5)
    #latitude and longiutude for google maps, e.g., 420 Grand Ave is 40.686529, -73.949413, not sure if engative sing counts as digit    
    date_joined_waitlist = models.DateTimeField('Date Joined Waitlist', blank=True, null=True)
    referred_by = models.CharField("Waitlist Referred By", max_length=254, blank=True, null=True)
    hostsinterest = models.BooleanField("Interested in Hosting", blank=True, default=False)
    #Attributes to add later/with functions
    fulluser = models.BooleanField("Full User", blank=True, default=False)
    address_latitude = models.DecimalField('Latitude Coordinate', max_digits=9, decimal_places=6, blank=True, null=True) #latitude is max-min 90, -90
    address_longitude = models.DecimalField('Longitude Coordinate', max_digits=10, decimal_places=6, blank=True, null=True) #longitude is max-min 180, -180
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, blank=True) #upate this so drop-down 
    #Will be blank 
    last_name = models.CharField('Last Name', max_length=100, blank=True)