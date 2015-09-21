# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_transaction_host_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='host_issue',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Host Issue', blank=True),
        ),
    ]
