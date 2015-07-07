# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0008_auto_20150625_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='sort_order',
            field=models.IntegerField(default=2),
        ),
    ]
