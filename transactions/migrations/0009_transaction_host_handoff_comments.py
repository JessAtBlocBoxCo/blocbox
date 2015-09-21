# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_auto_20150912_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='host_handoff_comments',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
