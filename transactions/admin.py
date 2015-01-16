from django.contrib import admin
from transactions.models import Transaction

class TransactionAdmin(admin.ModelAdmin): 
    list_display = ('id', 'payment_processed', 'trans_complete', 'on_aftership', 'enduser', 'host', 'title', 'favortype', 'date_requested', 'tracking', 'invoice', 'price', 'enduser_rating',)
    list_filter = ['host', 'enduser', 'favortype']
    search_fields = ['host', 'enduser']  

admin.site.register(Transaction, TransactionAdmin)