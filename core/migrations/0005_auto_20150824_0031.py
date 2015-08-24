# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_userinfo_hostuserinterest'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='offers_autocare',
            field=models.BooleanField(default=False, verbose_name=b'Offers Letting Auto Care'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_carsharing',
            field=models.BooleanField(default=False, verbose_name=b'Offers Car Sharing'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_childcare',
            field=models.BooleanField(default=False, verbose_name=b'Offers Childcare'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_housemaint',
            field=models.BooleanField(default=False, verbose_name=b'Offers House Maintenance'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_housesitting',
            field=models.BooleanField(default=False, verbose_name=b'Offers  HouseSitting'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_laundry',
            field=models.BooleanField(default=False, verbose_name=b'Offers Laundry'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_lawn',
            field=models.BooleanField(default=False, verbose_name=b'Offers Letting Lawn Care'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_letin',
            field=models.BooleanField(default=False, verbose_name=b'Offers Letting Maintenance Person Into Home'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_petcare',
            field=models.BooleanField(default=False, verbose_name=b'Offers Petcare'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_plantcare',
            field=models.BooleanField(default=False, verbose_name=b'Offers Plantcare'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_rentals',
            field=models.BooleanField(default=False, verbose_name=b'Offers Party/Equipment Rentals'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_storage',
            field=models.BooleanField(default=False, verbose_name=b'Offers Storage'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='offers_userdefined',
            field=models.BooleanField(default=False, verbose_name=b'User Defined Offers'),
        ),
    ]
