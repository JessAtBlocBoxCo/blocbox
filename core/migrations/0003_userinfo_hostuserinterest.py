# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_userinfo_betauser_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='hostuserinterest',
            field=models.BooleanField(default=False, verbose_name=b'Host Interested in Using Blocbox'),
        ),
    ]
