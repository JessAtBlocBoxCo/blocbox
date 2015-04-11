from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from waitlist.models import Waitlist
from django.core.validators import validate_email

class WaitlistForm(forms.Form):
		email=forms.CharField(max_length=254, required=False)
		first_name=forms.CharField(max_length=50, required=False)
		zipcode=forms.CharField(max_length=5, required=False)
		referred_by=forms.CharField(max_length=254, required=False)
		hostinterest=forms.BooleanField(default=False)

#Contact us form - on www.blocbox.co/support and www/blocbox.co/contactus
class ContactUs(forms.Form): 
    contactus_subject=forms.CharField(max_length=150, required=False)
    contactus_body = forms.CharField(max_length=1000, required=False)
    reply_to_email = forms.EmailField(required=False)
    
#The hostPRofileForm should include the UserProfileForm and other stuff specific to host
#Need a second about_me field for hosts that is required
class HostForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('host_aboutme', 'services_offered', 'availability', 'hostrating',)
   
#connect form for useres that are already registered, still works off of userinfo 
#NOTE - I DONT THINK THIS IS IN USE, DELETE IF NOT
class ConnectForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('about_me', 'intro_message', 'pickup_time', 'FBlink', 'imageurl', 'userrating', 'host',
            'need_storage', 'need_petcare', 'need_housesitting', 'need_rentals', 'need_laundry', 'need_letin',
    				'need_childcare', 'need_plantcare', 'need_lawn', 'need_carsharing', 'need_housemaint', 'need_autocare', 'need_other'
            )


#NotificationSettings form
class NotificationSettings(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('notifyuser_hostnewtask', 'notifyuser_message', 'notifyuser_packageships', 'notifyuser_newhostonblock',
    						'notifyuser_deliveryexception', 'notifyuser_packagereceived', 'notifyuser_blocboxnews', 
    						'notifyuser_trackinginfo', 'zipcodes_nearby_mileradius')
    						
