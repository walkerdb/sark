# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0005_radioshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_link', models.FilePathField(max_length=200, path='C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/audio', match='.*\\.mp3')),
            ],
        ),
        migrations.AddField(
            model_name='radioshow',
            name='audio',
            field=models.ForeignKey(default=0, to='sark.Audio'),
            preserve_default=False,
        ),
    ]
