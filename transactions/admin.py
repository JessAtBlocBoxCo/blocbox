from django.contrib import admin
from transactions.models import Transaction

class TransactionAdmin(admin.ModelAdmin): 
    list_display = ('id', 'enduser', 'host', 'favortype', 'date_requested', 'status', 'tracking', 'price', 'deliverydatenotracking_rangeend')
    list_filter = ['host', 'enduser', 'favortype']
    search_fields = ['host', 'enduser']  

admin.site.register(Transaction, TransactionAdmin)