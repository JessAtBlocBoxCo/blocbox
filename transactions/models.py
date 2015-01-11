from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
#from django.contrib.auth.models import User #need to include this b/c we reference that table (auth_user in django db)
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#import core models
from core.models import UserInfo
from connections.models import Connection


class Transaction(models.Model):
	  #need related_name to define relationship to user table because there are two
	  #MAY NEED TO UPDATE THIS TO settings.AUTH_USER_MODEL
    #payer = models.ForeignKey(UserInfo, related_name='payer') #each transaction related to payer from the delmeusers
    #payee = models.ForeignKey(UserInfo, related_name='payee') #each ransaction related to payee that is a user on delmeusers
    host = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='transaction_host', blank=True, null=True) #this shows up as payer_id
    enduser = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='transaction_enduser', blank=True, null=True) #thius shiws up as payee_id
    #host = models.CharField("Host/Provider", max_length=100, blank=True, null=True)
    #enduser = models.CharField("EndUser/Receiver", max_length=100, blank=True, null=True)
    price = models.DecimalField('Amount Paid', max_digits=6, decimal_places=2, blank=True, null=True)   
    date_requested = models.DateTimeField(default=datetime.datetime.today)
    date_requested_notime = models.DateField(default = datetime.date.today, null=True)
    favortype = models.CharField("Favor Type", max_length=100, blank=True, null=True)
    invoice = models.CharField("Invoice ID", max_length=100, blank=True, null=True)
    tracking = models.CharField("Tracking Number", max_length=50, blank=True, null=True)
    status = models.CharField("Status", max_length=50, blank=True, null=True)
    favorstatus = models.CharField("Favor Status (Non-Shipments)", max_length=50, blank=True, null=True)
    dayrangestart = models.IntegerField("Package Arrival Range Start", blank=True, null=True)
    dayrangeend = models.IntegerField("Package Arrival Range End", blank=True, null=True)
    #to get a date use DateField (datetime.date.today), to get date with time use DateTimeField
    #datenow = models.DateField("Date When Requested (Duplicative but needed)", blank=True, null=True)
    deliverydatenotracking_rangestart = models.DateField("Expected Delivery Date Range Start, Before Tracking Information Entered", blank=True, null=True)
    deliverydatenotracking_rangeend = models.DateField("Delivered By (No Tracking)", blank=True, null=True)
    deliverydate_tracking = models.DateField("Expected Delivery Date Pulled from Tracking Information", blank=True, null=True)
    testfieldagain = models.CharField("test field", max_length=50, blank=True, null=True)
    #End user Complete Transaction and rating
    trans_complete = models.BooleanField("Transaction Complete", null=True, default=False, required=False) 
    RATING_CHOICES = ( (1, 0.2), (2, 0.4), (3, 0.6), (4, 0.8), (5, 1.0) )
    enduser_rating = models.DecimalField(max_length=2, decimal_places=1, choices=RATING_CHOICES, blank=True, null=True)
    enduser_comments = models.CharField("EndUser Transaction Comments", max_length=200, blank=True, null=True)
    #Report an issue
    enduser_issue = models.CharField("EndUser Issue", max_length=300, blank=True, null=True)


"""Remove the transaction type choices field - could add these back later, now will  link to other defs 
    #define transaciton type choices
    PACKAGE='Package'
    STORAGE='Storage'
    PETCARE='Petcare'
    HOUSESITTING='HouseSitting'
    RENTALS='Rentals'
    LAUNDRY='Laundry'
    LETIN='Letin'
    CHILDCARE='ChildCare'
    PLANTCARE='PlantCare'
    LAWN='Lawn'
    CARSHARING='CarSharing'
    HOUSEMAINT='HouseMaint'
    AUTOCARE='AutoCare'
    OTHER='Other'
    TYPE_CHOICES = ((PACKAGE, 'Package'), (STORAGE, 'Storage'), (PETCARE, 'Pet Care'), 
        (HOUSESITTING, 'House Sitting'), (RENTALS, 'Equipment Rental'), (LAUNDRY, 'Laundry'), 
        (LETIN, 'Let Someone In House'), (CHILDCARE, 'Child Care'), (PLANTCARE, 'Plant Care'), (LAWN, 'Lawn Care'),
        (CARSHARING, 'Car Sharing'), (HOUSEMAINT, 'House Maintenance'), (AUTOCARE, 'Auto Maintenance'),
        (OTHER, 'Other'))
    transtype = models.CharField('Transaction Type', max_length=30, choices=TYPE_CHOICES, default=PACKAGE) #transaction type           
"""  

