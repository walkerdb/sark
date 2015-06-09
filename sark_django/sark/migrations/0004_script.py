# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('plaintext_link', models.FilePathField(match='.*\\.txt', path='C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/scripts', max_length=200)),
            ],
        ),
    ]
