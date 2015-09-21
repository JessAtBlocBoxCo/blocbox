# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0012_remove_transaction_host_received_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='host_received_datetime',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
