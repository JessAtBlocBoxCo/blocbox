# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transaction'
        db.create_table(u'transactions_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='payer', null=True, to=orm['core.UserInfo'])),
            ('enduser', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='payee', null=True, to=orm['core.UserInfo'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('date_requested', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date.today)),
            ('favortype', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('invoice', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('tracking', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('shipmentstatus', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('deliverydate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('favorstatus', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'transactions', ['Transaction'])


    def backwards(self, orm):
        # Deleting model 'Transaction'
        db.delete_table(u'transactions_transaction')


    models = {
        u'core.userinfo': {
            'FBlink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'Meta': {'object_name': 'UserInfo'},
            'about_me': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'address_approx': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'availability': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
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
        },
        u'transactions.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'date_requested': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date.today'}),
            'deliverydate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'enduser': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'payee'", 'null': 'True', 'to': u"orm['core.UserInfo']"}),
            'favorstatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'favortype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'payer'", 'null': 'True', 'to': u"orm['core.UserInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'shipmentstatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tracking': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['transactions']