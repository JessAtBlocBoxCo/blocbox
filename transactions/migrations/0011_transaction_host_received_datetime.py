# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_auto_20150921_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='host_received_datetime',
            field=models.DateField(null=True, blank=True),
        ),
    ]
