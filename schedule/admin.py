from django.contrib import admin

from schedule.models import Calendar, Event, CalendarRelation, Rule

class CalendarAdminOptions(admin.ModelAdmin):
	  list_display = ('id', 'slug',)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']


admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register([Rule, Event, CalendarRelation])
