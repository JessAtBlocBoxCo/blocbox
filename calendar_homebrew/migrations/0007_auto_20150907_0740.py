# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendar_homebrew', '0006_auto_20150907_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostConflicts_DateVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.IntegerField(verbose_name=b'Conflict Day')),
                ('month', models.IntegerField(verbose_name=b'Conflict Month')),
                ('year', models.IntegerField(verbose_name=b'Conflict Year')),
                ('date', models.DateField(null=True, verbose_name=b'Conflict Date', blank=True)),
                ('host', models.ForeignKey(related_name='host_conflict_dateversion', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion_onetable',
            name='host',
            field=models.ForeignKey(related_name='host_conflict_dateversion_manytables', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
