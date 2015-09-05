# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='days_until_delivery',
            field=models.IntegerField(null=True, verbose_name=b'Days Until Delivery', blank=True),
        ),
    ]
