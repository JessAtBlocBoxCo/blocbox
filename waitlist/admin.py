from django.contrib import admin
from django import forms
from waitlist.models import Waitlist

# Register your models here.
class WaitlistAdmin(admin.ModelAdmin):
    #just list 'pass' if you want it to id just the email address and then they clik on it to see other fields
    #pass
    list_display = ('id', 'fulluser', 'email', 'zipcode', 'first_name', 'hostinterest', 'referred_by', )
    list_filter = ['zipcode', 'fulluser' ]
    search_fields = ['email', 'first_name', 'zipcode']  
    
admin.site.register(Waitlist, WaitlistAdmin)
admin.site.unregister(Group)