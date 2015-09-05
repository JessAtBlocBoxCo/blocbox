# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_user_last_login_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='FBlink',
            field=models.URLField(null=True, verbose_name=b'Facebook Profile Link', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='facebook_first_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='facebook_last_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='full_name',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Full Name', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='intro_message',
            field=models.CharField(max_length=350, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pickup_time',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
