# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Transaction.cal_checkbox1'
        db.delete_column(u'transactions_transaction', 'cal_checkbox1')

        # Deleting field 'Transaction.cal_checkbox3'
        db.delete_column(u'transactions_transaction', 'cal_checkbox3')

        # Deleting field 'Transaction.cal_checkbox2'
        db.delete_column(u'transactions_transaction', 'cal_checkbox2')

        # Deleting field 'Transaction.cal_checkbox5'
        db.delete_column(u'transactions_transaction', 'cal_checkbox5')

        # Deleting field 'Transaction.cal_checkbox4'
        db.delete_column(u'transactions_transaction', 'cal_checkbox4')

        # Deleting field 'Transaction.cal_checkbox7'
        db.delete_column(u'transactions_transaction', 'cal_checkbox7')

        # Deleting field 'Transaction.cal_checkbox6'
        db.delete_column(u'transactions_transaction', 'cal_checkbox6')

        # Adding field 'Transaction.arrivalwindow_day1'
        db.add_column(u'transactions_transaction', 'arrivalwindow_day1',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.arrivalwindow_day2'
        db.add_column(u'transactions_transaction', 'arrivalwindow_day2',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.arrivalwindow_day3'
        db.add_column(u'transactions_transaction', 'arrivalwindow_day3',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.arrivalwindow_day4'
        db.add_column(u'transactions_transaction', 'arrivalwindow_day4',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.arrivalwindow_day5'
        db.add_column(u'transactions_transaction', 'arrivalwindow_day5',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.arrivalwindow_day6'
        db.add_column(u'transactions_transaction', 'arrivalwindow_day6',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.arrivalwindow_day7'
        db.add_column(u'transactions_transaction', 'arrivalwindow_day7',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Transaction.cal_checkbox1'
        db.add_column(u'transactions_transaction', 'cal_checkbox1',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.cal_checkbox3'
        db.add_column(u'transactions_transaction', 'cal_checkbox3',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.cal_checkbox2'
        db.add_column(u'transactions_transaction', 'cal_checkbox2',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.cal_checkbox5'
        db.add_column(u'transactions_transaction', 'cal_checkbox5',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.cal_checkbox4'
        db.add_column(u'transactions_transaction', 'cal_checkbox4',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.cal_checkbox7'
        db.add_column(u'transactions_transaction', 'cal_checkbox7',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.cal_checkbox6'
        db.add_column(u'transactions_transaction', 'cal_checkbox6',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Transaction.arrivalwindow_day1'
        db.delete_column(u'transactions_transaction', 'arrivalwindow_day1')

        # Deleting field 'Transaction.arrivalwindow_day2'
        db.delete_column(u'transactions_transaction', 'arrivalwindow_day2')

        # Deleting field 'Transaction.arrivalwindow_day3'
        db.delete_column(u'transactions_transaction', 'arrivalwindow_day3')

        # Deleting field 'Transaction.arrivalwindow_day4'
        db.delete_column(u'transactions_transaction', 'arrivalwindow_day4')

        # Deleting field 'Transaction.arrivalwindow_day5'
        db.delete_column(u'transactions_transaction', 'arrivalwindow_day5')

        # Deleting field 'Transaction.arrivalwindow_day6'
        db.delete_column(u'transactions_transaction', 'arrivalwindow_day6')

        # Deleting field 'Transaction.arrivalwindow_day7'
        db.delete_column(u'transactions_transaction', 'arrivalwindow_day7')


    models = {
        u'core.userinfo': {
            'FBlink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'Meta': {'object_name': 'UserInfo'},
            'about_me': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'address_approx': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'address_longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'availability': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'customchar': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'customcharthree': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'customchartwo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'favorscompleted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'favorsrequested': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'host': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'host_aboutme': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'hostinterest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostrating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'intro_message': ('django.db.models.fields.CharField', [], {'max_length': '350', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'need_autocare': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_carsharing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_childcare': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_housemaint': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_housesitting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_laundry': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_lawn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_letin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_petcare': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_plantcare': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_rentals': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_storage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'pickup_time': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'price_package_annual': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'price_package_bundle10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'price_package_month20': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'price_package_per': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'profile_pic_uploaded': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'services_offered': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'st_address1': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'st_address2': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'userrating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'whenimhome_days': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'whenimhome_hours': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'transactions.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'arrivalwindow_day1': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'arrivalwindow_day2': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'arrivalwindow_day3': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'arrivalwindow_day4': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'arrivalwindow_day5': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'arrivalwindow_day6': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'arrivalwindow_day7': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_completed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_requested': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 1, 0, 0)'}),
            'date_requested_notime': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True'}),
            'datetime_completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dayrangeend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dayrangestart': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'deliverydate_tracking': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deliverydatenotracking_rangeend': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deliverydatenotracking_rangestart': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'enduser': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'transaction_enduser'", 'null': 'True', 'to': u"orm['core.UserInfo']"}),
            'enduser_comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'enduser_issue': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'enduser_rating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'favorstatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'favortype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'transaction_host'", 'null': 'True', 'to': u"orm['core.UserInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'note_to_host': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'on_aftership': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'payment_option': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'payment_processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'paypal_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'shipment_courier': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'testfieldagain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tracking': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tracking_info_tuple_confirmd': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'trans_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'youselected': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['transactions']