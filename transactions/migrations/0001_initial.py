# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(null=True, verbose_name=b'Price', max_digits=6, decimal_places=2, blank=True)),
                ('amount_due', models.DecimalField(null=True, verbose_name=b'Amount Due', max_digits=6, decimal_places=2, blank=True)),
                ('payment_option', models.CharField(max_length=30, null=True, verbose_name=b'Payment Option', blank=True)),
                ('payment_method', models.CharField(max_length=20, null=True, verbose_name=b'Payment Method', blank=True)),
                ('payment_needed', models.BooleanField(default=False)),
                ('balance_created_packages', models.IntegerField(null=True, blank=True)),
                ('balance_before_packages', models.IntegerField(null=True, blank=True)),
                ('balance_after_packages', models.IntegerField(null=True, blank=True)),
                ('youselected', models.CharField(max_length=50, null=True, blank=True)),
                ('paypal_quantity', models.IntegerField(null=True, blank=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'Title', blank=True)),
                ('note_to_host', models.CharField(max_length=200, null=True, verbose_name=b'Note to Host from User', blank=True)),
                ('payment_processed', models.BooleanField(default=False, verbose_name=b'Paid')),
                ('date_requested', models.DateTimeField(default=datetime.datetime.today)),
                ('date_requested_notime', models.DateField(default=datetime.date.today, null=True)),
                ('favortype', models.CharField(max_length=100, null=True, verbose_name=b'Favor Type', blank=True)),
                ('invoice', models.CharField(max_length=100, null=True, verbose_name=b'Invoice ID', blank=True)),
                ('tracking', models.CharField(max_length=50, null=True, verbose_name=b'Tracking Number', blank=True)),
                ('status', models.CharField(max_length=50, null=True, verbose_name=b'Status', blank=True)),
                ('favorstatus', models.CharField(max_length=50, null=True, verbose_name=b'Favor Status (Non-Shipments)', blank=True)),
                ('arrivalwindow_days_count', models.IntegerField(null=True, blank=True)),
                ('arrivalwindow_day1', models.DateField(null=True, blank=True)),
                ('arrivalwindow_day2', models.DateField(null=True, blank=True)),
                ('arrivalwindow_day3', models.DateField(null=True, blank=True)),
                ('arrivalwindow_day4', models.DateField(null=True, blank=True)),
                ('arrivalwindow_day5', models.DateField(null=True, blank=True)),
                ('arrivalwindow_day6', models.DateField(null=True, blank=True)),
                ('arrivalwindow_day7', models.DateField(null=True, blank=True)),
                ('arrivalwindow_lastday', models.DateField(null=True, blank=True)),
                ('arrivalwindow_string', models.CharField(max_length=200, null=True, blank=True)),
                ('deliverydatenotracking_rangestart', models.DateField(null=True, verbose_name=b'Expected Delivery Date Range Start, Before Tracking Information Entered', blank=True)),
                ('deliverydatenotracking_rangeend', models.DateField(null=True, verbose_name=b'Delivered By (No Tracking)', blank=True)),
                ('deliverydate_tracking', models.DateField(null=True, verbose_name=b'Expected Delivery Date Pulled from Tracking Information', blank=True)),
                ('testfieldagain', models.CharField(max_length=50, null=True, verbose_name=b'test field', blank=True)),
                ('trans_complete', models.BooleanField(default=False, verbose_name=b'Complete?')),
                ('trans_archived', models.BooleanField(default=False, verbose_name=b'Archived?')),
                ('datetime_completed', models.DateTimeField(null=True, blank=True)),
                ('date_completed', models.DateField(null=True, blank=True)),
                ('enduser_rating', models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1, choices=[(1, 0.2), (2, 0.4), (3, 0.6), (4, 0.8), (5, 1.0)])),
                ('enduser_comments', models.CharField(max_length=200, null=True, verbose_name=b'EndUser Transaction Comments', blank=True)),
                ('enduser_issue', models.CharField(max_length=300, null=True, verbose_name=b'EndUser Issue', blank=True)),
                ('on_aftership', models.BooleanField(default=False, verbose_name=b'Aftership')),
                ('aftership_expired', models.BooleanField(default=False, verbose_name=b'Expired?')),
                ('shipment_courier', models.CharField(max_length=20, null=True, verbose_name=b'Courier', blank=True)),
                ('tracking_info_tuple_confirmd', models.CharField(max_length=2000, null=True, verbose_name=b'Aftership Tracking Info Tuple Upon Completion', blank=True)),
                ('last_tracking_status', models.CharField(max_length=75, null=True, blank=True)),
                ('last_tracking_date', models.DateField(null=True, blank=True)),
                ('last_tracking_datetime', models.DateTimeField(null=True, blank=True)),
                ('last_checkpoint_city', models.CharField(max_length=40, null=True, blank=True)),
                ('last_checkpoint_state', models.CharField(max_length=25, null=True, blank=True)),
                ('last_checkpoint_datetime', models.DateTimeField(null=True, blank=True)),
                ('last_checkpoint_date', models.DateField(null=True, blank=True)),
                ('dayrangestart', models.IntegerField(null=True, verbose_name=b'Min. Shipping Days', blank=True)),
                ('dayrangeend', models.IntegerField(null=True, verbose_name=b'Max. Shipping Days', blank=True)),
                ('enduser', models.ForeignKey(related_name='transaction_enduser', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('host', models.ForeignKey(related_name='transaction_host', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
