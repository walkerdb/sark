# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0003_auto_20150624_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='radioshow',
            old_name='photos',
            new_name='images',
        ),
        migrations.AlterField(
            model_name='radioshow',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='radioshow',
            name='description',
            field=models.CharField(blank=True, max_length=200, default=''),
            preserve_default=False,
        ),
    ]
