# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0012_transaction_host_received_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='host_handoff_datetime',
            field=models.DateField(null=True, blank=True),
        ),
    ]
