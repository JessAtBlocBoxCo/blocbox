from django.contrib import admin
from calendar_homebrew.models import HostConflicts_DateVersion_OneTable, HostConflicts_OldVersion, HostConflicts_BooleanVersion, HostWeeklyDefaultSchedule

class ConflictsAdmin_DateVersion_OneTable(admin.ModelAdmin): 
    list_display = ('id', 'host', )
    list_filter = ['host',  ]
    search_fields = ['host', ]  

class ConflictsAdmin_BooleanVersion(admin.ModelAdmin): 
    list_display = ('id', 'host', )
    list_filter = ['host',  ]
    search_fields = ['host', ]  

class ConflictsAdmin_OldVersion(admin.ModelAdmin): 
    list_display = ('id', 'host', 'label', 'date_from', 'date_to', 'duration', 'allday',)
    list_filter = ['host',  ]
    search_fields = ['host', ]  

class WeeklyScheduleAdmin(admin.ModelAdmin): 
    list_display = ('id', 'host', 'monday_available', 'tuesday_available', 'wednesday_available', 'thursday_available', 'friday_available', 'saturday_available', 'sunday_available',)
    list_filter = ['host',]
    search_fields = ['host',  ] 

admin.site.register(HostConflicts_DateVersion_OneTable, ConflictsAdmin_DateVersion_OneTable)
admin.site.register(HostConflicts_BooleanVersion, ConflictsAdmin_BooleanVersion)
admin.site.register(HostConflicts_OldVersion, ConflictsAdmin_OldVersion)
admin.site.register(HostWeeklyDefaultSchedule, WeeklyScheduleAdmin)