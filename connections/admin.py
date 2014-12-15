from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from connections.models import Connection
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
    AdminPasswordChangeForm)
 

class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('host_user', 'end_user', 'added')
    list_filter = ['host_user']
    search_fields = ['host_user', 'end_user']

admin.site.register(Connection, ConnectionAdmin)