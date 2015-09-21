# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_auto_20150920_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='host_received',
            new_name='host_received_datetime',
        ),
    ]
