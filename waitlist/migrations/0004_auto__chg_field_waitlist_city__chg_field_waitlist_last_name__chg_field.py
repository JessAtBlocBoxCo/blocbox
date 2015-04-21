# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Waitlist.city'
        db.alter_column(u'waitlist_waitlist', 'city', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Waitlist.last_name'
        db.alter_column(u'waitlist_waitlist', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Waitlist.state'
        db.alter_column(u'waitlist_waitlist', 'state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

    def backwards(self, orm):

        # Changing field 'Waitlist.city'
        db.alter_column(u'waitlist_waitlist', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'Waitlist.last_name'
        db.alter_column(u'waitlist_waitlist', 'last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Waitlist.state'
        db.alter_column(u'waitlist_waitlist', 'state', self.gf('django.db.models.fields.CharField')(default='', max_length=2))

    models = {
        u'waitlist.waitlist': {
            'Meta': {'object_name': 'Waitlist'},
            'address_latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'address_longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'date_joined_waitlist': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fulluser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostinterest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'referred_by': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['waitlist']