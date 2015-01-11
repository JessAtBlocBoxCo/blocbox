from django.contrib import admin
from transactions.models import Transaction

class TransactionAdmin(admin.ModelAdmin): 
    list_display = ('id', 'trans_complete', 'enduser', 'host', 'favortype', 'date_requested', 'tracking', 'price', 'deliverydatenotracking_rangeend', 'enduser_rating')
    list_filter = ['host', 'enduser', 'favortype']
    search_fields = ['host', 'enduser']  

admin.site.register(Transaction, TransactionAdmin)