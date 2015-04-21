# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Waitlist.zipcodes_nearby'
        db.add_column(u'waitlist_waitlist', 'zipcodes_nearby',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Waitlist.zipcodes_nearby_mileradius'
        db.add_column(u'waitlist_waitlist', 'zipcodes_nearby_mileradius',
                      self.gf('django.db.models.fields.IntegerField')(default=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Waitlist.neighbors_1mileradius'
        db.add_column(u'waitlist_waitlist', 'neighbors_1mileradius',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Waitlist.neighbors_2mileradius'
        db.add_column(u'waitlist_waitlist', 'neighbors_2mileradius',
                      self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Waitlist.neighbors_3mileradius'
        db.add_column(u'waitlist_waitlist', 'neighbors_3mileradius',
                      self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Waitlist.neighbors_4mileradius'
        db.add_column(u'waitlist_waitlist', 'neighbors_4mileradius',
                      self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Waitlist.neighbors_5mileradius'
        db.add_column(u'waitlist_waitlist', 'neighbors_5mileradius',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Waitlist.zipcodes_nearby'
        db.delete_column(u'waitlist_waitlist', 'zipcodes_nearby')

        # Deleting field 'Waitlist.zipcodes_nearby_mileradius'
        db.delete_column(u'waitlist_waitlist', 'zipcodes_nearby_mileradius')

        # Deleting field 'Waitlist.neighbors_1mileradius'
        db.delete_column(u'waitlist_waitlist', 'neighbors_1mileradius')

        # Deleting field 'Waitlist.neighbors_2mileradius'
        db.delete_column(u'waitlist_waitlist', 'neighbors_2mileradius')

        # Deleting field 'Waitlist.neighbors_3mileradius'
        db.delete_column(u'waitlist_waitlist', 'neighbors_3mileradius')

        # Deleting field 'Waitlist.neighbors_4mileradius'
        db.delete_column(u'waitlist_waitlist', 'neighbors_4mileradius')

        # Deleting field 'Waitlist.neighbors_5mileradius'
        db.delete_column(u'waitlist_waitlist', 'neighbors_5mileradius')


    models = {
        u'waitlist.waitlist': {
            'Meta': {'object_name': 'Waitlist'},
            'address_latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'address_longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'date_joined_waitlist': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fulluser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostinterest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'neighbors_1mileradius': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'neighbors_2mileradius': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'neighbors_3mileradius': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'neighbors_4mileradius': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'neighbors_5mileradius': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'referred_by': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'zipcodes_nearby': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'zipcodes_nearby_mileradius': ('django.db.models.fields.IntegerField', [], {'default': '2', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['waitlist']