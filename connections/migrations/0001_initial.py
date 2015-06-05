# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateField(default=datetime.date.today)),
                ('intro_message', models.CharField(max_length=300, null=True, verbose_name=b'Intro Message to Host from User', blank=True)),
                ('pickup_time', models.CharField(max_length=150, null=True, verbose_name=b'Preferred Pickup Time', blank=True)),
                ('testfield', models.CharField(max_length=200, null=True, blank=True)),
                ('end_user', models.ForeignKey(related_name='enduser_id', to=settings.AUTH_USER_MODEL)),
                ('host_user', models.ForeignKey(related_name='host_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together=set([('host_user', 'end_user')]),
        ),
    ]
