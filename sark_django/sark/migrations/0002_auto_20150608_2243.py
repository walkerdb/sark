# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='role',
        ),
        migrations.RemoveField(
            model_name='radioshow',
            name='host',
        ),
        migrations.RemoveField(
            model_name='radioshow',
            name='script',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='RadioShow',
        ),
        migrations.DeleteModel(
            name='Script',
        ),
    ]
