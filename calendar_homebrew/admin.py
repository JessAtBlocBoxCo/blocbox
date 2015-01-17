from django.contrib import admin
from calendar_homebrew.models import HostConflicts, HostWeeklyDefaultSchedule

class ConflictsAdmin(admin.ModelAdmin): 
    list_display = ('id', 'host', 'host_email', 'label', 'date_from', 'date_to', 'allday',)
    list_filter = ['host', 'host_email', ]
    search_fields = ['host', 'host_email', ]  

class WeeklyScheduleAdmin(admin.ModelAdmin): 
    list_display = ('id', 'host', 'host_email', 'monday_available', 'tuesday_available', 'wednesday_available', 'thursday_available', 'friday_available', 'saturday_available', 'sundahy_available',)
    list_filter = ['host', 'host_email', ]
    search_fields = ['host', 'host_email', ] 
    
admin.site.register(HostConflicts, ConflictsAdmin)
admin.site.register(HostWeeklyDefaultSchedule, WeeklyScheduleAdmin)