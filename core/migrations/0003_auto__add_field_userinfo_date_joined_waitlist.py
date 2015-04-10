# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserInfo.date_joined_waitlist'
        db.add_column(u'core_userinfo', 'date_joined_waitlist',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserInfo.date_joined_waitlist'
        db.delete_column(u'core_userinfo', 'date_joined_waitlist')


    models = {
        u'core.userinfo': {
            'FBlink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'Meta': {'object_name': 'UserInfo'},
            'about_me': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'account_balance_packages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'address_approx': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'address_longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'availability': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'customchar': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'customcharthree': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'customchartwo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'date_joined_waitlist': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'facebook_email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'facebook_first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'facebook_gender': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'facebook_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'facebook_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'facebook_locale': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'facebook_response_all': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'facebook_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'favorscompleted': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'favorsrequested': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fulluser': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'neighbors_1mileradius': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'neighbors_2mileradius': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'neighbors_3mileradius': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'neighbors_4mileradius': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'neighbors_5mileradius': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'notifyuser_blocboxnews': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notifyuser_deliveryexception': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notifyuser_hostnewtask': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notifyuser_message': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notifyuser_newhostonblock': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notifyuser_packagereceived': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notifyuser_packageships': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notifyuser_trackinginfo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'pickup_time': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'price_package_annual': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'price_package_bundle10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'price_package_bundle20': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'price_package_per': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'profile_pic_uploaded': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'services_offered': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'st_address1': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'st_address2': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'userrating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'waitlistuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'whenimhome_days': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'whenimhome_hours': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'zipcodes_nearby': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'zipcodes_nearby_mileradius': ('django.db.models.fields.IntegerField', [], {'default': '2', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']