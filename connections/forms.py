from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from core.models import UserInfo
from connections.models import Connection
   
#connect form for useres that are already registered, still works off of userinfo 
class ConnectForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = ('intro_message', 'pickup_time','host_user', 'end_user')

