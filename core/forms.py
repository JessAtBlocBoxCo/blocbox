from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from core.models import UserInfo
from connections.models import Connection

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    zipcode = forms.CharField(label="Zip Code")

    class Meta:
        model = UserInfo
        fields = ('email', 'password', 'password2', 'zipcode', 'hostinterest', 
            'first_name', 'last_name', 'zipcode', 'st_address1', 'st_address2', 'city', 'state',
            'about_me', 'intro_message', 'pickup_time', 'FBlink', 'imageurl', 'userrating', 'host',
            'need_storage', 'need_petcare', 'need_housesitting', 'need_rentals', 'need_laundry', 'need_letin',
    				'need_childcare', 'need_plantcare', 'need_lawn', 'need_carsharing', 'need_housemaint', 'need_autocare', 'need_other'
            )
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
        fields = ('notifyuser_hostnewtask', 'notifyuser_message', 'notifyuser_packageships',
    						'notifyuser_packageissue', 'notifyuser_packagereceived', 'notifyuser_blocboxnews', 'notifyuser_trackinginfo')
    						
