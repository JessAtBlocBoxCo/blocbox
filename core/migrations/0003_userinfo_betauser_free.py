# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150824_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='betauser_free',
            field=models.BooleanField(default=True),
        ),
    ]
