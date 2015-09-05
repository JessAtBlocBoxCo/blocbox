# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_days_until_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='last_checkpoint_message',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
