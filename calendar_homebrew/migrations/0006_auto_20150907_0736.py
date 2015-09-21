# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendar_homebrew', '0005_auto_20150907_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostConflicts_DateVersion_OneTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thimonthconflict1', models.DateField(null=True, blank=True)),
                ('thimonthconflict2', models.DateField(null=True, blank=True)),
                ('thimonthconflict3', models.DateField(null=True, blank=True)),
                ('thimonthconflict4', models.DateField(null=True, blank=True)),
                ('thimonthconflict5', models.DateField(null=True, blank=True)),
                ('thimonthconflict6', models.DateField(null=True, blank=True)),
                ('thimonthconflict7', models.DateField(null=True, blank=True)),
                ('thimonthconflict8', models.DateField(null=True, blank=True)),
                ('thimonthconflict9', models.DateField(null=True, blank=True)),
                ('thimonthconflict10', models.DateField(null=True, blank=True)),
                ('thimonthconflict11', models.DateField(null=True, blank=True)),
                ('thimonthconflict12', models.DateField(null=True, blank=True)),
                ('thimonthconflict13', models.DateField(null=True, blank=True)),
                ('thimonthconflict14', models.DateField(null=True, blank=True)),
                ('thimonthconflict15', models.DateField(null=True, blank=True)),
                ('thimonthconflict16', models.DateField(null=True, blank=True)),
                ('thimonthconflict17', models.DateField(null=True, blank=True)),
                ('thimonthconflict18', models.DateField(null=True, blank=True)),
                ('thimonthconflict19', models.DateField(null=True, blank=True)),
                ('thimonthconflict20', models.DateField(null=True, blank=True)),
                ('thimonthconflict21', models.DateField(null=True, blank=True)),
                ('thimonthconflict22', models.DateField(null=True, blank=True)),
                ('thimonthconflict23', models.DateField(null=True, blank=True)),
                ('thimonthconflict24', models.DateField(null=True, blank=True)),
                ('thimonthconflict25', models.DateField(null=True, blank=True)),
                ('thimonthconflict26', models.DateField(null=True, blank=True)),
                ('thimonthconflict27', models.DateField(null=True, blank=True)),
                ('thimonthconflict28', models.DateField(null=True, blank=True)),
                ('thimonthconflict29', models.DateField(null=True, blank=True)),
                ('thimonthconflict30', models.DateField(null=True, blank=True)),
                ('thimonthconflict31', models.DateField(null=True, blank=True)),
                ('nextmonthconflict1', models.DateField(null=True, blank=True)),
                ('nextmonthconflict2', models.DateField(null=True, blank=True)),
                ('nextmonthconflict3', models.DateField(null=True, blank=True)),
                ('nextmonthconflict4', models.DateField(null=True, blank=True)),
                ('nextmonthconflict5', models.DateField(null=True, blank=True)),
                ('nextmonthconflict6', models.DateField(null=True, blank=True)),
                ('nextmonthconflict7', models.DateField(null=True, blank=True)),
                ('nextmonthconflict8', models.DateField(null=True, blank=True)),
                ('nextmonthconflict9', models.DateField(null=True, blank=True)),
                ('nextmonthconflict10', models.DateField(null=True, blank=True)),
                ('nextmonthconflict11', models.DateField(null=True, blank=True)),
                ('nextmonthconflict12', models.DateField(null=True, blank=True)),
                ('nextmonthconflict13', models.DateField(null=True, blank=True)),
                ('nextmonthconflict14', models.DateField(null=True, blank=True)),
                ('nextmonthconflict15', models.DateField(null=True, blank=True)),
                ('nextmonthconflict16', models.DateField(null=True, blank=True)),
                ('nextmonthconflict17', models.DateField(null=True, blank=True)),
                ('nextmonthconflict18', models.DateField(null=True, blank=True)),
                ('nextmonthconflict19', models.DateField(null=True, blank=True)),
                ('nextmonthconflict20', models.DateField(null=True, blank=True)),
                ('nextmonthconflict21', models.DateField(null=True, blank=True)),
                ('nextmonthconflict22', models.DateField(null=True, blank=True)),
                ('nextmonthconflict23', models.DateField(null=True, blank=True)),
                ('nextmonthconflict24', models.DateField(null=True, blank=True)),
                ('nextmonthconflict25', models.DateField(null=True, blank=True)),
                ('nextmonthconflict26', models.DateField(null=True, blank=True)),
                ('nextmonthconflict27', models.DateField(null=True, blank=True)),
                ('nextmonthconflict28', models.DateField(null=True, blank=True)),
                ('nextmonthconflict29', models.DateField(null=True, blank=True)),
                ('nextmonthconflict30', models.DateField(null=True, blank=True)),
                ('nextmonthconflict31', models.DateField(null=True, blank=True)),
                ('host', models.ForeignKey(related_name='host_conflict_dateversion', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='hostconflicts_dateversion',
            name='host',
        ),
        migrations.DeleteModel(
            name='HostConflicts_DateVersion',
        ),
    ]
