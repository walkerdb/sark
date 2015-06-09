# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0006_auto_20150609_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='access_link',
            field=models.FilePathField(path='C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/audio', match='.*\\.mp3', max_length=200, default=0),
        ),
    ]
