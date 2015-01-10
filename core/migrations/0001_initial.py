# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserInfo'
        db.create_table(u'core_userinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('st_address1', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('st_address2', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('imageurl', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('host', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hostinterest', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hostrating', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('userrating', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2, blank=True)),
            ('favorscompleted', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('favorsrequested', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('FBlink', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('intro_message', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
            ('pickup_time', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('about_me', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('need_storage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_petcare', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_housesitting', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_rentals', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_laundry', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_letin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_childcare', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_plantcare', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_lawn', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_carsharing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_housemaint', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_autocare', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_other', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('neighborhood', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('services_offered', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('host_aboutme', self.gf('django.db.models.fields.CharField')(max_length=350, blank=True)),
            ('availability', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('whenimhome_days', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('whenimhome_hours', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('address_approx', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('customchar', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('customchartwo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('customcharthree', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['UserInfo'])


    def backwards(self, orm):
        # Deleting model 'UserInfo'
        db.delete_table(u'core_userinfo')


    models = {
        u'core.userinfo': {
            'FBlink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'Meta': {'object_name': 'UserInfo'},
            'about_me': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'address_approx': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'services_offered': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'st_address1': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'st_address2': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'userrating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'whenimhome_days': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'whenimhome_hours': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['core']