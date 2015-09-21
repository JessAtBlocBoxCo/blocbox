# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_transaction_host_handoff_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='host_received',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
