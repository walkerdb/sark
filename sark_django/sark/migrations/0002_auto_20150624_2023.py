# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('genre',)},
        ),
        migrations.AlterModelOptions(
            name='instrument',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ('country', 'name')},
        ),
        migrations.AlterModelOptions(
            name='performance',
            options={'ordering': ('date', 'title')},
        ),
        migrations.AlterModelOptions(
            name='radioshow',
            options={'ordering': ('date',)},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ('role',)},
        ),
        migrations.AlterField(
            model_name='performance',
            name='date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='location',
            field=models.ForeignKey(default='', to='sark.Location', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='performance',
            name='photos',
            field=models.ManyToManyField(blank=True, to='sark.Image'),
        ),
    ]
