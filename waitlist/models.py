from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings 

class Waitlist(models.Model): #standard fields defined below
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField('First Name',max_length=100, blank=True, null=True)    
    zipcode = models.CharField(max_length =5)
    #latitude and longiutude for google maps, e.g., 420 Grand Ave is 40.686529, -73.949413, not sure if engative sing counts as digit    
    date_joined_waitlist = models.DateTimeField('Date Joined Waitlist', default=timezone.now, blank=True, null=True)
    referredby = models.CharField("Waitlist Referred By", max_length=254, blank=True, null=True)
    hostinterest = models.BooleanField("Interested in Hosting", blank=True, default=False)
    #Attributes to add later/with functions
    fulluser = models.BooleanField("Full User", blank=True, default=False)
    address_latitude = models.DecimalField('Latitude Coordinate', max_digits=9, decimal_places=6, blank=True, null=True) #latitude is max-min 90, -90
    address_longitude = models.DecimalField('Longitude Coordinate', max_digits=10, decimal_places=6, blank=True, null=True) #longitude is max-min 180, -180
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True) #upate this so drop-down 
    #Zipcodes nearby
    zipcodes_nearby = models.CharField(max_length=1000, blank=True, null=True)
    zipcodes_nearby_mileradius = models.IntegerField(blank=True, null=True, default=2)
    neighbors_1mileradius = models.CharField(max_length=200, blank=True, null=True)
    neighbors_2mileradius = models.CharField(max_length=400, blank=True, null=True)
    neighbors_3mileradius = models.CharField(max_length=600, blank=True, null=True)
    neighbors_4mileradius = models.CharField(max_length=800, blank=True, null=True)
    neighbors_5mileradius = models.CharField(max_length=1000, blank=True, null=True)
    #Will be blank 
    last_name = models.CharField('Last Name', max_length=100, blank=True, null=True)