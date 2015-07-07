# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0005_auto_20150624_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='audio',
            field=models.FileField(null=True, upload_to='audio'),
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
    ]
