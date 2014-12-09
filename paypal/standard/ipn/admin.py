#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from paypal.standard.ipn.models import PayPalIPN


class PayPalIPNAdmin(admin.ModelAdmin):
    date_hierarchy = 'payment_date'
    fieldsets = (
        (None, {
            "fields": [
                "invoice", "payment_status", "payment_date",
                "receiver_email", "host_email", "payer_email", "custom", 
                "item_name", "quantity", "mc_gross",
                "flag", "txn_id", "txn_type",
                "transaction_entity", "reason_code", "pending_reason",
                "mc_currency", "mc_fee", "mc_handling", "mc_shipping",
                "auth_status", "auth_amount", "auth_exp", "auth_id"
            ]
        }),
        ("Address", {
            "description": "The address of the Buyer.",
            'classes': ('collapse',),
            "fields": [
                "address_city", "address_country", "address_country_code",
                "address_name", "address_state", "address_status",
                "address_street", "address_zip"
            ]
        }),
        ("End User/Buyer", {
            "description": "Additional information about the End User/Payer.",
            'classes': ('collapse',),
            "fields": [
                "first_name", "last_name", "payer_business_name",
                "payer_id", "payer_status", "contact_phone", "residence_country"
            ]
        }),
        ("Host/Seller", {
            "description": "Additional information about the Host.",
            'classes': ('collapse',),
            "fields": [
                "business", "host_fname", "host_lname", "host_st_address1", "host_st_address2",  
                "item_number", "receiver_id", "memo"
            ]
        }),
        ("Recurring", {
            "description": "Information about recurring Payments.",
            "classes": ("collapse",),
            "fields": [
                "profile_status", "initial_payment_amount", "amount_per_cycle",
                "outstanding_balance", "period_type", "product_name",
                "product_type", "recurring_payment_id", "receipt_id",
                "next_payment_date"
            ]
        }),
        ("Admin", {
            "description": "Additional Info.",
            "classes": ('collapse',),
            "fields": [
                "test_ipn", "ipaddress", "query", "response", "flag_code",
                "flag_info"
            ]
        }),
    )
    list_display = [
        #JMY edited this. 
        #"__unicode__", - this is defined with a functionin paypal.standard.models.py - it outputs the TX Id
        #"receiver_id",
        "invoice", "receiver_email",  "host_email", "custom", "payer_email", "item_name", "quantity", "mc_gross", "payment_status", "created_at", 
    ]
    #"flag","flag_info", -- removing flag itself from the list above
    search_fields = ["txn_id", "recurring_payment_id"]


admin.site.register(PayPalIPN, PayPalIPNAdmin)