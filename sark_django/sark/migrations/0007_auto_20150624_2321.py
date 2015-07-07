# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0006_auto_20150624_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radioshow',
            options={'ordering': ('broadcast_date',)},
        ),
        migrations.RenameField(
            model_name='radioshow',
            old_name='date',
            new_name='broadcast_date',
        ),
    ]
