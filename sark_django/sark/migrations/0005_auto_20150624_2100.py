# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0004_auto_20150624_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioshow',
            name='images',
            field=models.ManyToManyField(blank=True, to='sark.Image'),
        ),
    ]
