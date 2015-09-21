# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendar_homebrew', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostConflicts_OldVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_from', models.DateField(null=True)),
                ('date_to', models.DateField(null=True, blank=True)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('allday', models.BooleanField(default=False, verbose_name=b'All Day?')),
                ('am', models.BooleanField(default=False, verbose_name=b'AM Conflict')),
                ('pm', models.BooleanField(default=False, verbose_name=b'PM Conflict')),
                ('time_from', models.TimeField(null=True, verbose_name=b'Time: From', blank=True)),
                ('time_to', models.TimeField(null=True, verbose_name=b'Time: To', blank=True)),
                ('datetime_added', models.DateTimeField(default=datetime.datetime.today, null=True, blank=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True, verbose_name=b'Date Conflict Added by Host', blank=True)),
                ('note', models.CharField(max_length=200, null=True, blank=True)),
                ('label', models.CharField(max_length=50, null=True, blank=True)),
                ('host', models.ForeignKey(related_name='host_conflict', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='hostconflicts',
            name='host',
        ),
        migrations.DeleteModel(
            name='HostConflicts',
        ),
    ]
