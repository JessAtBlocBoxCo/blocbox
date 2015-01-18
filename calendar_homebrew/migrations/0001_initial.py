# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HostConflicts'
        db.create_table(u'calendar_homebrew_hostconflicts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='host_conflict', null=True, to=orm['core.UserInfo'])),
            ('date_from', self.gf('django.db.models.fields.DateField')(null=True)),
            ('date_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('allday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('am', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pm', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('time_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('datetime_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 16, 0, 0), null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateField')(default=datetime.date.today, null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'calendar_homebrew', ['HostConflicts'])

        # Adding model 'HostWeeklyDefaultSchedule'
        db.create_table(u'calendar_homebrew_hostweeklydefaultschedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='host_weeklyschedule', null=True, to=orm['core.UserInfo'])),
            ('monday_available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tuesday_available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wednesday_available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('thursday_available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('friday_available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('saturday_available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sunday_available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('default_time1_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('default_time1_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('default_time2_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('default_time2_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('default_time3_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('default_time3_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('default_time4_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('default_time4_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('monday_time1_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('monday_time1_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('monday_time2_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('monday_time2_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('monday_time3_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('monday_time3_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('monday_time4_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('monday_time4_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('tuesday_time1_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('tuesday_time1_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('tuesday_time2_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('tuesday_time2_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('tuesday_time3_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('tuesday_time3_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('tuesday_time4_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('tuesday_time4_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('wednesday_time1_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('wednesday_time1_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('wednesday_time2_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('wednesday_time2_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('wednesday_time3_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('wednesday_time3_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('wednesday_time4_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('wednesday_time4_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thursday_time1_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thursday_time1_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thursday_time2_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thursday_time2_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thursday_time3_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thursday_time3_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thursday_time4_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thursday_time4_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('friday_time1_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('friday_time1_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('friday_time2_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('friday_time2_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('friday_time3_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('friday_time3_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('friday_time4_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('friday_time4_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('saturday_time1_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('saturday_time1_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('saturday_time2_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('saturday_time2_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('saturday_time3_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('saturday_time3_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('saturday_time4_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('saturday_time4_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sunday_time1_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sunday_time1_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sunday_time2_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sunday_time2_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sunday_time3_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sunday_time3_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sunday_time4_from', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sunday_time4_to', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('monday_note', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('tuesday_note', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('wednesday_note', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('thursday_note', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('friday_note', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('saturday_note', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('sunday_note', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('date_schedule_created', self.gf('django.db.models.fields.DateField')(default=datetime.date.today, null=True, blank=True)),
            ('date_last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 16, 0, 0), null=True, blank=True)),
        ))
        db.send_create_signal(u'calendar_homebrew', ['HostWeeklyDefaultSchedule'])


    def backwards(self, orm):
        # Deleting model 'HostConflicts'
        db.delete_table(u'calendar_homebrew_hostconflicts')

        # Deleting model 'HostWeeklyDefaultSchedule'
        db.delete_table(u'calendar_homebrew_hostweeklydefaultschedule')


    models = {
        u'calendar_homebrew.hostconflicts': {
            'Meta': {'object_name': 'HostConflicts'},
            'allday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'am': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True', 'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'datetime_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 16, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'host_conflict'", 'null': 'True', 'to': u"orm['core.UserInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'calendar_homebrew.hostweeklydefaultschedule': {
            'Meta': {'object_name': 'HostWeeklyDefaultSchedule'},
            'date_last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 16, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'date_schedule_created': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True', 'blank': 'True'}),
            'default_time1_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_time1_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_time2_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_time2_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_time3_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_time3_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_time4_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_time4_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'friday_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'friday_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'friday_time1_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'friday_time1_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'friday_time2_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'friday_time2_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'friday_time3_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'friday_time3_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'friday_time4_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'friday_time4_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'host_weeklyschedule'", 'null': 'True', 'to': u"orm['core.UserInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'monday_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'monday_time1_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'monday_time1_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'monday_time2_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'monday_time2_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'monday_time3_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'monday_time3_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'monday_time4_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'monday_time4_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'saturday_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'saturday_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'saturday_time1_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'saturday_time1_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'saturday_time2_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'saturday_time2_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'saturday_time3_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'saturday_time3_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'saturday_time4_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'saturday_time4_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sunday_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sunday_time1_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_time1_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_time2_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_time2_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_time3_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_time3_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_time4_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunday_time4_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thursday_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'thursday_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'thursday_time1_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thursday_time1_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thursday_time2_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thursday_time2_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thursday_time3_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thursday_time3_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thursday_time4_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thursday_time4_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tuesday_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tuesday_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tuesday_time1_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tuesday_time1_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tuesday_time2_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tuesday_time2_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tuesday_time3_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tuesday_time3_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tuesday_time4_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tuesday_time4_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wednesday_available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wednesday_note': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wednesday_time1_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wednesday_time1_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wednesday_time2_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wednesday_time2_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wednesday_time3_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wednesday_time3_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wednesday_time4_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wednesday_time4_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
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

    complete_apps = ['calendar_homebrew']