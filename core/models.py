from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings

#from django.contrib.auth.models import User #need to include this b/c we reference that table (auth_user in django db)
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


#NEED TO CREATE A MANAGER FOR THE USER MODEL
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        #creates ad saves a user with given email and password
        if not email:
            raise ValueError('Users must have an email address')
    
        user = self.model(email=self.normalize_email(email))
    
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class UserInfo(AbstractBaseUser): #standard fields defined below
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField('First Name',max_length=100, blank=True)
    last_name = models.CharField('Last Name', max_length=100, blank=True)
    zipcode = models.CharField(max_length =5)
    st_address1 = models.CharField('Street Address 1', max_length = 70, blank=True)
    st_address2 = models.CharField('Street Address 2', max_length = 70, blank=True)
    #latitude and longiutude for google maps, e.g., 420 Grand Ave is 40.686529, -73.949413, not sure if engative sing counts as digit
    address_latitude = models.DecimalField('Latitude Coordinate', max_digits=9, decimal_places=6, blank=True, null=True) #latitude is max-min 90, -90
    address_longitude = models.DecimalField('Longitude Coordinate', max_digits=10, decimal_places=6, blank=True, null=True) #longitude is max-min 180, -180
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, blank=True) #upate this so drop-down 
    #The picture field isn't working i need to isntal the imagefield thing... will do later.. for now use linktoimage
    #picture = models.ImageField(upload_to='profile_images', blank=True)  
    imageurl= models.URLField('Profile Picture URL', blank=True)
    host = models.BooleanField(blank=True, default=False) #boolean can't be null if want null need NullBooleanField
    hostinterest = models.BooleanField('Interested in Hosting', blank=True, default=False)
    hostrating = models.DecimalField('Host Rating', max_digits=3, decimal_places=2, blank=True, null=True)
    userrating = models.DecimalField('User Rating',max_digits=3,decimal_places=2, blank=True, null=True)
    favorscompleted = models.IntegerField('Favors Completed',blank=True, null=True)
    favorsrequested = models.IntegerField('Favors Requested',blank=True, null=True)
    FBlink = models.URLField('Facebook Profile Link', blank=True)
    intro_message = models.CharField(max_length=350, blank=True) #Intro Message to Host
    pickup_time = models.CharField(max_length=150, blank=True) 
    #the following i thought were on AbstractBaseUser but aren't showing up
    #had to set a lot of these up as blank=true because of custom form may want to rechange later
    is_admin = models.BooleanField('Admin User',default=False, blank=True)
    is_active = models.BooleanField('Active User',default=True, blank=True)
    date_joined = models.DateTimeField('Date Joined', default=timezone.now, blank=True, null=True) #auto_now_add auto_now_add=True
    about_me = models.CharField('About Me', max_length=300, blank=True)
    #add other request options
    need_storage = models.BooleanField('May Need Storage', blank=True, default=False)
    need_petcare = models.BooleanField('May Need Petcare', blank=True, default=False)
    need_housesitting = models.BooleanField('May Need HouseSitting', blank=True, default=False)
    need_rentals = models.BooleanField('May Need Party/Equipment Rentals', blank=True, default=False)
    need_laundry = models.BooleanField('May Need Laundry', blank=True, default=False)
    need_letin = models.BooleanField('May Need Letting Maintenance Person Into Home', blank=True, default=False)
    need_childcare=models.BooleanField('May Need Childcare', blank=True, default=False)
    need_plantcare=models.BooleanField('May Need Plantcare', blank=True, default=False)
    need_lawn=models.BooleanField('May Need Letting Lawn Care', blank=True, default=False)
    need_carsharing=models.BooleanField('May Need Car Sharing', blank=True, default=False)
    need_housemaint=models.BooleanField('May Need House Maintenance', blank=True, default=False) 	 	
    need_autocare=models.BooleanField('May Need Letting Auto Care', blank=True, default=False)
    need_other=models.BooleanField('May Need Other Task/REquests', blank=True, default=False)
    
    neighborhood = models.CharField("Neighborhood Name", max_length=100, blank=True, null=True)
    phone_number = models.CharField("Phone Number", max_length=12, blank=True, null=True)
    
		#Add more host-specific fields
		#!!! Note - maybe move this to host table that is linked to user table - may make it easeri to connect
    services_offered = models.CharField('UPDATE TO CHOICES - SERVICES\q OFFERED', max_length=250, blank=True)
    host_aboutme = models.CharField("About Me (Host)",max_length=350,blank=True)
    availability = models.CharField("Availability (Write-In)",max_length=250,blank=True)
    whenimhome_days = models.CharField("When I'm Home: Days of the Week (Write-In)",max_length=250,blank=True)
    whenimhome_hours = models.CharField("When I'm Home: Hours (Write-In)",max_length=250,blank=True)
    address_approx = models.CharField("Approximate Address for Visitors to See", max_length=100, blank=True, null=True) 
    
    #addingj custom or text fields
    customchar = models.CharField("Custom Character field to edit later", max_length=200, blank=True, null=True)
    customchartwo = models.CharField("Custom Character Field second version", max_length=200, blank=True, null=True)
    customcharthree = models.CharField("Custom CharacterField third version", max_length=100, blank=True, null=True)
    #Create manytomany connections - neighbors are those connected to
    #neighbors = models.ManyToManyField("self", through='Connections') 
    #neighbors = models.ManyToManyField("self")
    
	  #Fields i am adding that were in AUTH user that we should have and populate later 
    """	fields that are on the AbstractBaseUser, is_active is_superuser last_login date_joined
    		however, is_active, is_superuser and date_joined are not showing up
    """
    #define these functios so that the foreignkey knows what to reference
    def __str__(self):
       return self.email
    def __unicode__(self):
       return self.email
       
    objects = MyUserManager() #Assigns MAnager to the Ojbects variable - needed to avoid attribute error
    
    #need to define a username field - this is the unique identifier
    USERNAME_FIELD = 'email'
    #define required fields
    REQUIRED_FIELDS = [] #blank right now - nothing is required
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
