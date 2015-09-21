# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_homebrew', '0004_auto_20150907_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='host',
            field=models.ForeignKey(related_name='host_conflict_dateversion', default=2, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict1',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict10',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict11',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict12',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict13',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict14',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict15',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict16',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict17',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict18',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict19',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict2',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict20',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict21',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict22',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict23',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict24',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict25',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict26',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict27',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict28',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict29',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict3',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict30',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict31',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict4',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict5',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict6',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict7',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict8',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='nextmonthconflict9',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict1',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict10',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict11',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict12',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict13',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict14',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict15',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict16',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict17',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict18',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict19',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict2',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict20',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict21',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict22',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict23',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict24',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict25',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict26',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict27',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict28',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict29',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict3',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict30',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict31',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict4',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict5',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict6',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict7',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict8',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hostconflicts_dateversion',
            name='thimonthconflict9',
            field=models.DateField(null=True, blank=True),
        ),
    ]
