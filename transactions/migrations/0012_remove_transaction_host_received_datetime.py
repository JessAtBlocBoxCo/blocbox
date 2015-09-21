# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_auto_20150920_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='host_received_datetime',
        ),
    ]
