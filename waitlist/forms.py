from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from waitlist.models import Waitlist
from django.core.validators import validate_email

class WaitlistForm(forms.Form):
    email = forms.CharField(max_length=254, required=False)
    first_name = forms.CharField(max_length=50, required=False)
    zipcode = forms.CharField(max_length=5, required=False)
    referredby = forms.CharField(max_length=254, required=False)
#    fulluser = forms.BooleanField(default=False)
    
class WaitlistFormModel(forms.ModelForm):
		class Meta:
		    model = Waitlist
		    fields = ('email', 'first_name', 'zipcode', 'referredby' )
