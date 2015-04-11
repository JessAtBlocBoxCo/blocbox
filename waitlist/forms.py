from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from waitlist.models import Waitlist
from django.core.validators import validate_email

#class WaitListForm(forms.Form):
#    email = forms.CharField(max_length=254, required=False)
#    first_name = forms.CharField(max_length=50, required=False)
#    zipcode = forms.CharField(max_lenght=5, required=False)
#    referred_by = forms.CharField(max_lenght=254, required=False)
#    fulluser = forms.BooleanField(default=False)
    
class WaitlistForm(forms.ModelForm):
		class Meta:
		    model = Waitlist
		    fields = ('email', 'first_name', 'zipcode', )
