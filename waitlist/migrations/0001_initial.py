# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Waitlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name=b'First Name', blank=True)),
                ('zipcode', models.CharField(max_length=5)),
                ('date_joined_waitlist', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name=b'Date Joined Waitlist', blank=True)),
                ('referredby', models.CharField(max_length=254, null=True, verbose_name=b'Waitlist Referred By', blank=True)),
                ('hostinterest', models.BooleanField(default=False, verbose_name=b'Interested in Hosting')),
                ('fulluser', models.BooleanField(default=False, verbose_name=b'Full User')),
                ('address_latitude', models.DecimalField(null=True, verbose_name=b'Latitude Coordinate', max_digits=9, decimal_places=6, blank=True)),
                ('address_longitude', models.DecimalField(null=True, verbose_name=b'Longitude Coordinate', max_digits=10, decimal_places=6, blank=True)),
                ('city', models.CharField(max_length=30, null=True, blank=True)),
                ('state', models.CharField(max_length=2, null=True, blank=True)),
                ('zipcodes_nearby', models.CharField(max_length=1000, null=True, blank=True)),
                ('zipcodes_nearby_mileradius', models.IntegerField(default=2, null=True, blank=True)),
                ('neighbors_1mileradius', models.CharField(max_length=200, null=True, blank=True)),
                ('neighbors_2mileradius', models.CharField(max_length=400, null=True, blank=True)),
                ('neighbors_3mileradius', models.CharField(max_length=600, null=True, blank=True)),
                ('neighbors_4mileradius', models.CharField(max_length=800, null=True, blank=True)),
                ('neighbors_5mileradius', models.CharField(max_length=1000, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name=b'Last Name', blank=True)),
                ('responseobject', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
    ]
