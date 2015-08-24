# -*- coding: utf-8 -*-
#found on: https://github.com/django/django/tree/master/django/contrib/auth/migrations
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150824_0031'), #'0006_alter_user_username_opts'), #changing 'auth' to 'core'
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
    ]