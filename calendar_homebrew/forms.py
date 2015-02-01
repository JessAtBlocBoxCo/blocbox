from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
import datetime

#calendar check boxes form
class CalendarCheckBoxes(forms.Form): #note this is not a model form
    month1day1  = forms.BooleanField(required=False)
    month1day2  = forms.BooleanField(required=False)
    month1day3  = forms.BooleanField(required=False)
    month1day4  = forms.BooleanField(required=False)
    month1day5  = forms.BooleanField(required=False)
    month1day6  = forms.BooleanField(required=False)
    month1day7  = forms.BooleanField(required=False)
    month1day8  = forms.BooleanField(required=False)
    month1day9  = forms.BooleanField(required=False)
    month1day10 = forms.BooleanField(required=False)
    month1day11 = forms.BooleanField(required=False)
    month1day12 = forms.BooleanField(required=False)
    month1day13 = forms.BooleanField(required=False)
    month1day14 = forms.BooleanField(required=False)
    month1day15 = forms.BooleanField(required=False)
    month1day16 = forms.BooleanField(required=False)
    month1day17 = forms.BooleanField(required=False)
    month1day18 = forms.BooleanField(required=False)
    month1day19 = forms.BooleanField(required=False)
    month1day20 = forms.BooleanField(required=False)
    month1day21 = forms.BooleanField(required=False)
    month1day22 = forms.BooleanField(required=False)
    month1day23 = forms.BooleanField(required=False)
    month1day24 = forms.BooleanField(required=False)
    month1day25 = forms.BooleanField(required=False)
    month1day26 = forms.BooleanField(required=False)
    month1day27 = forms.BooleanField(required=False)
    month1day28 = forms.BooleanField(required=False)
    month1day29 = forms.BooleanField(required=False)
    month1day30 = forms.BooleanField(required=False)
    month1day31 = forms.BooleanField(required=False)
    month2day1  = forms.BooleanField(required=False)
    month2day2  = forms.BooleanField(required=False)
    month2day3  = forms.BooleanField(required=False)
    month2day4  = forms.BooleanField(required=False)
    month2day5  = forms.BooleanField(required=False)
    month2day6  = forms.BooleanField(required=False)
    month2day7  = forms.BooleanField(required=False)
    month2day8  = forms.BooleanField(required=False)
    month2day9  = forms.BooleanField(required=False)
    month2day10 = forms.BooleanField(required=False)
    month2day11 = forms.BooleanField(required=False)
    month2day12 = forms.BooleanField(required=False)
    month2day13 = forms.BooleanField(required=False)
    month2day14 = forms.BooleanField(required=False)
    month2day15 = forms.BooleanField(required=False)
    month2day16 = forms.BooleanField(required=False)
    month2day17 = forms.BooleanField(required=False)
    month2day18 = forms.BooleanField(required=False)
    month2day19 = forms.BooleanField(required=False)
    month2day20 = forms.BooleanField(required=False)
    month2day21 = forms.BooleanField(required=False)
    month2day22 = forms.BooleanField(required=False)
    month2day23 = forms.BooleanField(required=False)
    month2day24 = forms.BooleanField(required=False)
    month2day25 = forms.BooleanField(required=False)
    month2day26 = forms.BooleanField(required=False)
    month2day27 = forms.BooleanField(required=False)
    month2day28 = forms.BooleanField(required=False)
    month2day29 = forms.BooleanField(required=False)
    month2day30 = forms.BooleanField(required=False)
    month2day31 = forms.BooleanField(required=False)
    
"""
    day1 = forms.DateField() 
    day2 = forms.DateField(required=False)
    day3 = forms.DateField(required=False)
    day4 = forms.DateField(required=False)
    day5 = forms.DateField(required=False)
    day6 = forms.DateField(required=False)
    day7 = forms.DateField(required=False)
"""
"""
    datechoices = forms.MultipleChoiceField(
        #choices = LIST_OF_VALID_CHOICES, # this is optional
        widget  = forms.CheckboxSelectMultiple,
    )
"""    
""" - EXAMPLE FROM THE TRANSACTIONS APP
class CreatePackageTransaction(forms.Form): 
    title = forms.CharField(max_length=100, required=False)
    payment_option = forms.CharField(max_length=30)
    note_to_host = forms.CharField(max_length=200, required=False)
"""