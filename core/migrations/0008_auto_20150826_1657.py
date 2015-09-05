# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150826_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='host_availability_writein',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='host_unavailability_writein',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='st_address1',
            field=models.CharField(max_length=70, null=True, verbose_name=b'Street Address 1', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='st_address2',
            field=models.CharField(max_length=70, null=True, verbose_name=b'Street Address 2', blank=True),
        ),
    ]
