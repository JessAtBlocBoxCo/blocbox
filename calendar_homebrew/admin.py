from django.contrib import admin
from calendar_homebrew.models import HostConflicts, HostWeeklyDefaultSchedule

class ConflictsAdmin(admin.ModelAdmin): 
    list_display = ('id', 'host', 'label', 'date_from', 'date_to', 'allday',)
    list_filter = ['host',  ]
    search_fields = ['host', ]  

class WeeklyScheduleAdmin(admin.ModelAdmin): 
    list_display = ('id', 'host', 'monday_available', 'tuesday_available', 'wednesday_available', 'thursday_available', 'friday_available', 'saturday_available', 'sunday_available',)
    list_filter = ['host',]
    search_fields = ['host',  ] 
    
admin.site.register(HostConflicts, ConflictsAdmin)
admin.site.register(HostWeeklyDefaultSchedule, WeeklyScheduleAdmin)