from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
import datetime

#calendar check boxes form
class CalendarCheckBoxes(forms.Form): #note this is not a model form
    day1 = forms.DateField() 
    day2 = forms.DateField(required=False)
    day3 = forms.DateField(required=False)
    day4 = forms.DateField(required=False)
    day5 = forms.DateField(required=False)
    day6 = forms.DateField(required=False)
    day7 = forms.DateField(required=False)
    day8 = forms.DateField(required=False)
    day9 = forms.DateField(required=False)
    day10 = forms.DateField(required=False)
""" - EXAMPLE FROM THE TRANSACTIONS APP
class CreatePackageTransaction(forms.Form): 
    title = forms.CharField(max_length=100, required=False)
    payment_option = forms.CharField(max_length=30)
    note_to_host = forms.CharField(max_length=200, required=False)
"""