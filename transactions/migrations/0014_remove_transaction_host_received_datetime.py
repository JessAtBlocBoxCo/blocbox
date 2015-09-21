# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0013_transaction_host_received_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='host_received_datetime',
        ),
    ]
