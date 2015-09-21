# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_transaction_host_received'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='host_received_comments',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
