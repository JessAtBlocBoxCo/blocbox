from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
from core.models import UserInfo
from transactions.models import Transaction

#Create a form to add the pricing optioninformation and the title
#the other fields are automatically added to the transactions table - though this could be changed
class CreatePackageTransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('title', 'payment_option', 
            #The remaining fields will be hidden input
            'host', 'enduser', 'dayrangestart', 'dayrangeend', 'invoice', 'price', 'deliverydatenotracking_rangestart', 'deliverydatenotracking_rangeend',)
        
class TrackingForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('tracking',)


class ModifyTransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('status',)    

class PackageReceived(forms.ModelForm):
	  class Meta:
	  		model = Transaction
	  		fields = ('trans_complete', 'enduser_rating', 'enduser_comments',)

class EndUserIssue(forms.ModelForm):
		class Meta:
				model = Transaction
				fields = ('enduser_issue',)


"""
  
#connect form for useres that are already registered, still works off of userinfo 
class ConnectForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('about_me', 'intro_message', 'pickup_time', 'FBlink', 'imageurl', 'userrating', 'host',
            'need_storage', 'need_petcare', 'need_housesitting', 'need_rentals', 'need_laundry', 'need_letin',
    				'need_childcare', 'need_plantcare', 'need_lawn', 'need_carsharing', 'need_housemaint', 'need_autocare', 'need_other'
            )
"""
