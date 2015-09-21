# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_transaction_host_received_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='host_issue',
            field=models.CharField(max_length=300, null=True, verbose_name=b'EndUser Issue', blank=True),
        ),
    ]
