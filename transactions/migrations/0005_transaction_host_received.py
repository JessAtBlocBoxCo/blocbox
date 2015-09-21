# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20150902_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='host_received',
            field=models.BooleanField(default=False),
        ),
    ]
