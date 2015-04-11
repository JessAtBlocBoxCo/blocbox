from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from waitlist.models import Waitlist
from django.core.validators import validate_email

class WaitlistForm(forms.ModelForm):
		class Meta:
		    model = Waitlist
		    fields = ('email', 'first_name', 'zipcode', 'referred_by', 'hostinterest',)
