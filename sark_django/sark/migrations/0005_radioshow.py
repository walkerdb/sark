# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sark', '0004_script'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadioShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('host', models.ForeignKey(to='sark.Person')),
                ('script', models.ForeignKey(to='sark.Script')),
            ],
        ),
    ]
