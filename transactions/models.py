from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
#from django.contrib.auth.models import User #need to include this b/c we reference that table (auth_user in django db)
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#import core models
from core.models import UserInfo, Connection


class Transaction(models.Model):
	  #need related_name to define relationship to user table because there are two
	  #MAY NEED TO UPDATE THIS TO settings.AUTH_USER_MODEL
    #payer = models.ForeignKey(UserInfo, related_name='payer') #each transaction related to payer from the delmeusers
    #payee = models.ForeignKey(UserInfo, related_name='payee') #each ransaction related to payee that is a user on delmeusers
    host = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='payer', blank=True, null=True) #this shows up as payer_id
    enduser = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='payee', blank=True, null=True) #thius shiws up as payee_id
    #host = models.CharField("Host/Provider", max_length=100, blank=True, null=True)
    #enduser = models.CharField("EndUser/Receiver", max_length=100, blank=True, null=True)
    price = models.DecimalField('Amount/Price of Transaction', max_digits=6, decimal_places=2, blank=True, null=True)   
    date_requested = models.DateTimeField(default=datetime.date.today)
    favortype = models.CharField("Transact/Favor Type", max_length=100, blank=True, null=True)
    invoice = models.CharField("Invoice ID", max_length=100, blank=True, null=True)
    tracking = models.CharField("Tracking Number", max_length=50, blank=True, null=True)
    status = models.CharField("Status", max_length=50, blank=True, null=True)
    shipmentstatus = models.CharField("Shipment Status", max_length=50, blank=True, null=True)
    deliverydate = models.DateField("Delivery Date", blank=True, null=True)
    favorstatus = models.CharField("Favor Status (Non-Shipments)", max_length=50, blank=True, null=True)
    
   
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

