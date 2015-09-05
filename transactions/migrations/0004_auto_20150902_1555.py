# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_transaction_last_checkpoint_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='days_until_delivery_est_end',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='days_until_delivery_est_start',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
