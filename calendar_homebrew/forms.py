from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings
import datetime
from calendar_homebrew.models import HostConflicts, HostWeeklyDefaultSchedule


#Hots Conflicts form
class HostConflictsForm(forms.ModelForm):
    class Meta:
        model = HostConflicts
        fields = ('host', 'date_from', 'date_to', 'duration', 'allday', 'am', 'pm', 'time_from', 'time_to', 'datetime_added', 'date_added',
            'note', 'label',
            )



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

    #JOHN - I ADDED THE TEXT FROM THIS POINT AND BELOW ON 8/28/2015 TO UPDATE IT TO THROW AND ERROR IF THE USER DID NOT SELECT ANY DATES ON THE CALENDAR
    #FIRST - I DEFINE THE ERROR MESSAGE
    error_messages = {  'no_dates_selected': "You have not selected any dates. Please select at least one approximate date on which you think the package may arrive.", }
    
    #NOTE -- IF YOU WANT TO WRITE A CUSTOM VALIDATION IT HAS TO BE CLEAN_(FIELD NAME) -- SEE https://docs.djangoproject.com/en/1.8/ref/forms/validation/
    #THIS IS COMPLICATED BECAUSE ITS ACTUALLY DEPENDENT ON THE VALUES FOR SEVERAL FIELDS
    #IN THIS INSTANCE WE USE THE CLEAN() METHOD BECAUSE IT APPLIES TO MULTIPLE FIELDS
    def clean(self):
    	  #The first part of the funciton defines each of the fields to be checked - before we run the validation thing - ths will make sense later
        month1day1 	 = self.cleaned_data.get("month1day1") 		    
        month1day2   = self.cleaned_data.get("month1day2")        
        month1day3   = self.cleaned_data.get("month1day3")        
        month1day4   = self.cleaned_data.get("month1day4")        
        month1day5   = self.cleaned_data.get("month1day5")        
        month1day6   = self.cleaned_data.get("month1day6")        
        month1day7   = self.cleaned_data.get("month1day7")        
        month1day8   = self.cleaned_data.get("month1day8")        
        month1day9   = self.cleaned_data.get("month1day9")        
        month1day10  = self.cleaned_data.get("month1day10")       
        month1day11  = self.cleaned_data.get("month1day11")       
        month1day12  = self.cleaned_data.get("month1day12")       
        month1day13  = self.cleaned_data.get("month1day13")       
        month1day14  = self.cleaned_data.get("month1day14")       
        month1day15  = self.cleaned_data.get("month1day15")       
        month1day16  = self.cleaned_data.get("month1day16")       
        month1day17  = self.cleaned_data.get("month1day17")       
        month1day18  = self.cleaned_data.get("month1day18")       
        month1day19  = self.cleaned_data.get("month1day19")       
        month1day20  = self.cleaned_data.get("month1day20")       
        month1day21  = self.cleaned_data.get("month1day21")       
        month1day22  = self.cleaned_data.get("month1day22")       
        month1day23  = self.cleaned_data.get("month1day23")       
        month1day24  = self.cleaned_data.get("month1day24")       
        month1day25  = self.cleaned_data.get("month1day25")       
        month1day26  = self.cleaned_data.get("month1day26")       
        month1day27  = self.cleaned_data.get("month1day27")       
        month1day28  = self.cleaned_data.get("month1day28")       
        month1day29  = self.cleaned_data.get("month1day29")       
        month1day30  = self.cleaned_data.get("month1day30")       
        month1day31  = self.cleaned_data.get("month1day31")      
        month2day1   = self.cleaned_data.get("month2day1")      
        month2day2   = self.cleaned_data.get("month2day2")      
        month2day3   = self.cleaned_data.get("month2day3")      
        month2day4   = self.cleaned_data.get("month2day4")      
        month2day5   = self.cleaned_data.get("month2day5")           
        month2day6   = self.cleaned_data.get("month2day6")           
        month2day7   = self.cleaned_data.get("month2day7")           
        month2day8   = self.cleaned_data.get("month2day8")           
        month2day9   = self.cleaned_data.get("month2day9")           
        month2day10 = self.cleaned_data.get("month2day10")          
        month2day11 = self.cleaned_data.get("month2day11")          
        month2day12 = self.cleaned_data.get("month2day12")          
        month2day13 = self.cleaned_data.get("month2day13")          
        month2day14 = self.cleaned_data.get("month2day14")          
        month2day15 = self.cleaned_data.get("month2day15")          
        month2day16 = self.cleaned_data.get("month2day16")          
        month2day17 = self.cleaned_data.get("month2day17")          
        month2day18 = self.cleaned_data.get("month2day18")          
        month2day19 = self.cleaned_data.get("month2day19")          
        month2day20 = self.cleaned_data.get("month2day20")          
        month2day21 = self.cleaned_data.get("month2day21")          
        month2day22 = self.cleaned_data.get("month2day22")          
        month2day23 = self.cleaned_data.get("month2day23")          
        month2day24 = self.cleaned_data.get("month2day24")          
        month2day25 = self.cleaned_data.get("month2day25")          
        month2day26 = self.cleaned_data.get("month2day26")          
        month2day27 = self.cleaned_data.get("month2day27")          
        month2day28 = self.cleaned_data.get("month2day28")          
        month2day29 = self.cleaned_data.get("month2day29")          
        month2day30 = self.cleaned_data.get("month2day30")          
        month2day31 = self.cleaned_data.get("month2day31")       
        #the second part of the function actually does the checking - this is one long if-then statement
        #it says - if none of the above defined variables are true (e.g., checked) then you throw the error - will documen thtat beelow
        if not ( month1day29 or month1day30 or \
            month1day2  or month2day2  or \
            month1day3  or month2day3  or \
            month1day4  or month2day4  or \
            month1day5  or month2day5  or \
            month1day6  or month2day6  or \
            month1day7  or month2day7  or \
            month1day8  or month2day8  or \
            month1day9  or month2day9  or \
            month1day10 or month2day10 or \
            month1day11 or month2day11 or \
            month1day12 or month2day12 or \
            month1day13 or month2day13 or \
            month1day14 or month2day14 or \
            month1day15 or month2day15 or \
            month1day16 or month2day16 or \
            month1day17 or month2day17 or \
            month1day18 or month2day18 or \
            month1day19 or month2day19 or \
            month1day20 or month2day20 or \
            month1day21 or month2day21 or \
            month1day22 or month2day22 or \
            month1day23 or month2day23 or \
            month1day24 or month2day24 or \
            month1day25 or month2day25 or \
            month1day26 or month2day26 or \
            month1day27 or month2day27 or \
            month1day28 or month2day28 or \
            month1day29 or month2day29 or \
            month1day30 or month2day30 or \
            month1day31 or month2day31 ) : 
            #this bottom part is what happens if none of them are true. it throws VAlidationError, and the error message 
            #is defined as no_dates_selected, which is defined above
            raise forms.ValidationError(
                self.error_messages['no_dates_selected'],
                code='no_dates_selected',
            )