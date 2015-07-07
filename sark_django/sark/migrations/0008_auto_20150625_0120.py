# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0007_auto_20150624_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioshow',
            name='script',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Script',
        ),
    ]
