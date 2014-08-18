from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from core.models import UserInfo, Transaction, Connection
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
    AdminPasswordChangeForm)

"""# get a way to log the errors:
import logging
log = logging.getLogger(__name__)
# convert the errors to text
from django.utils.encoding import force_text
"""

#Create a simpler admin interface
class UserInfoAdmin(admin.ModelAdmin):
    pass

class TransactionAdmin(admin.ModelAdmin):
    pass

class ConnectionAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Connection, ConnectionAdmin)

"""
#class UserCreationFormBB(forms.ModelForm):
#USERCREATION FORM AT DJANGO.CONTRIB.AUTH.FORMS
#class BBUserCreation(UserCreationForm):
class BBUserCreation(forms.ModelForm):
    #A form for creating new users. Includes all the required fields, plus a repeated password.
    #can find the base form at /usr/local/lib/python2.7/dist-packages/django/contrib/auth/forms.py
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    zipcode = forms.CharField(label="Zip Code")
    
    class Meta:
        model = UserInfo
        fields = ('email',) #it looks like this need a comma after it
        
    def clean_password2(self):    
        #check that the two password entries match - THIS PART IS WORKING
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        #save the provided password in hashed format
        user = super(BBUserCreation, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

        
#class UserChangeFormBB(forms.ModelForm):
class UserChangeFormBB(UserChangeForm):
    password = ReadOnlyPasswordHashField()
    
    model = UserInfo
    fields = ('email', 'password', 'is_active', 'is_admin')
    
    def clean_password(self):
        # Regardless of what the user provides, return the initial value
        # This is done here, rather  than on the field, because the field does not have access to the inital value
        return self.initial['password']
"""
      
#UserAdmin code is at /usr/local/lib/python2.7/dist-packages/django/contrib/auth/admin.py
#class UserAdmin(admin.ModelAdmin):     
"""
class BBUserAdmin(UserAdmin):
    #The forms to add and chage user instances
    add_form = BBUserCreation 
    form = UserChangeFormBB
    #add_form = UserCreationForm
    
    #from the file - contrib.auth.admin.py
    #form = UserChangeForm
    #add_form = UserCreationForm
    #add_form_template = /usr/local/lib/python2.7/dist-packages/django/contrib/admin/templates/admin/auth/user/add_form.html   
    #change_user_password_template = None
    
    list_display = ('id', 'email', 'password', 'is_admin', 'date_joined', 'zipcode', 'st_address1', 'st_address2', 'city', 'state', 'first_name', 'last_name', 'host', 'hostinterest')
    #(('question', 'pub_date', 'was_published_recently')		
    list_filter = ['zipcode', 'is_admin'] #add list_filter to allow filters by zipcode
    #Need to add fieldsets
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('zipcode', 'st_address1', 'st_address2', 'city', 'state', 'first_name', 'last_name')}),
        ('Host Info', {'fields': ('host', 'hostinterest')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    #add_fieldsets is not a standard ModelAdmin attribute. 
    #UserAdmin overrides get_fieldsets to use this when creating user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
        		'fields': ('email', 'password', 'password2', 'zipcode')}	
        ),
    )     
    search_fields = ['email', 'zipcode', 'last_name', 'first_name', 'st_address1', 'city'] #adds search box to change list - can search as many fields as you want, but harder with more fields
    #extra = 3 #add eough space for 3 extra entries
    ordering = ('email',) #may need this...
    filter_horizontal = () #may need this...

"""

"""   
class TransactionAdmin(admin.ModelAdmin): #Tabular instead of stacked to save screenspace  
    list_display = ('id', 'payer', 'payee', 'transtype', 'date_requested', 'date_payed')
    list_filter = ['transtype']
    search_fields = ['payer', 'payee']
    extra = 3 # provide enough fields for 3 

#Cannot register tabularinline as a class - onkly a subclass 



#unregister and re-resitger
admin.site.register(UserInfo, BBUserAdmin) #passes PollAdmin object
admin.site.register(Transaction, TransactionAdmin)
#unregister the group model from admin
admin.site.unregister(Group)

"""
