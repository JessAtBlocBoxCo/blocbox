# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='host_availability_writein',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='host_unavailability_writein',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='availability',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='host_aboutme',
            field=models.CharField(max_length=350, verbose_name=b'Host Intro Message', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='services_offered',
            field=models.CharField(max_length=250, verbose_name=b'Update to Choices Services Offered', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='whenimhome_days',
            field=models.CharField(max_length=250, verbose_name=b'Host Availability Days of Week', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='whenimhome_hours',
            field=models.CharField(max_length=250, verbose_name=b'Host Availability Hours of Day', blank=True),
        ),
    ]
