from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from core.models import UserInfo
from transactions.models import Transaction

#Create a form to add the pricing optioninformation and the title
#the other fields are automatically added to the transactions table - though this could be changed
class CreatePackageTransaction(forms.Form): #Note this is NOT a modelForm, the view saves the data from the form th trans
    title = forms.CharField(max_length=100, required=False)
    payment_option = forms.CharField(max_length=30)
    note_to_host = forms.CharField(max_length=200, required=False)
    packagedays_count = forms.IntegerField(required=False)
    arrivalwindow_day1 = forms.CharField(max_length=30, required=False) #needs to be in YYYY-MM-DD 
    arrivalwindow_day2 = forms.CharField(max_length=30, required=False)
    arrivalwindow_day3 = forms.CharField(max_length=30, required=False)
    arrivalwindow_day4 = forms.CharField(max_length=30, required=False)
    arrivalwindow_day5 = forms.CharField(max_length=30, required=False)
    arrivalwindow_day6 = forms.CharField(max_length=30, required=False)
    arrivalwindow_day7 = forms.CharField(max_length=30, required=False)
    arrivalwindow_day1string = forms.CharField(max_length=30, required=False) #needs to be in YYYY-MM-DD 
    arrivalwindow_day2string = forms.CharField(max_length=30, required=False)
    arrivalwindow_day3string = forms.CharField(max_length=30, required=False)
    arrivalwindow_day4string = forms.CharField(max_length=30, required=False)
    arrivalwindow_day5string = forms.CharField(max_length=30, required=False)
    arrivalwindow_day6string = forms.CharField(max_length=30, required=False)
    arrivalwindow_day7string = forms.CharField(max_length=30, required=False)   
   
        
class TrackingForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('tracking',)

class ModifyTransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('status',)

#rewriting this not based on the model because its not updating
class PackageReceived(forms.Form): 
    enduser_rating=forms.IntegerField(max_value=5, required=False)
    enduser_comments=forms.CharField(max_length=200, required=False)

class EndUserIssue(forms.ModelForm):
		class Meta:
				model = Transaction
				fields = ('enduser_issue',)

class MessageHost(forms.Form):
    message_body = forms.CharField(max_length=700, required=False)
    
class HostReceived(forms.Form):
    host_comments=forms.CharField(max_length=200, required=False)

    
