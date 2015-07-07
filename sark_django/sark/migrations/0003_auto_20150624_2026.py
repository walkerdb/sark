# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0002_auto_20150624_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='location',
            field=models.ForeignKey(blank=True, null=True, to='sark.Location'),
        ),
    ]
