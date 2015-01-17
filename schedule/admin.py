#this is blocbox.schedule.admin.py
from django.contrib import admin

from schedule.models import Calendar, Event, CalendarRelation, Rule

class CalendarAdminOptions(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']

class CalendarRelationAdmin(admin.ModelAdmin): 
    list_display = ('id', 'calendar', 'content_type_id', 'object_id', 'distinction',)
    list_filter = ['calendar', 'object_id', 'distinction']

admin.site.register(CalendarRelation, CalendarRelationAdmin)
admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register([Rule, Event,])
