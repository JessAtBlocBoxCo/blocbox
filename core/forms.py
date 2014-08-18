from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from core.models import UserInfo, Transaction

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

#The hostPRofileForm should include the UserProfileForm and other stuff specific to host
#Need a second about_me field for hosts that is required
class HostForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('host_aboutme', 'services_offered', 'availability', 'neighbors', 'hostrating',)

"""Meta Tags - describes additional properties about the particular ModelForm  class it belongs to. 
	Each Meta class must at a bare minimum supply a model field, which references back to the
	model the ModelForm inheriting class should relate to. 
"""       
        
        
