# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('deathdate', models.DateField(null=True, blank=True)),
                ('dates_active', models.CharField(max_length=20, null=True, blank=True)),
                ('bio', models.CharField(max_length=2000, default='No bio on record')),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('access_link', models.FilePathField(match='.*\\.mp3', max_length=200, default=0, path='C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/audio')),
            ],
            options={
                'verbose_name_plural': 'audio',
            },
        ),
        migrations.CreateModel(
            name='CopyrightStatus',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'copyright statuses',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentFamily',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('family', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'instrument families',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('zoom', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(null=True)),
                ('audio', models.ForeignKey(to='sark.Audio')),
                ('genres', models.ManyToManyField(blank=True, to='sark.Genre')),
                ('instruments', models.ManyToManyField(blank=True, to='sark.Instrument')),
                ('location', models.ForeignKey(to='sark.Location', null=True)),
                ('performers', models.ManyToManyField(blank=True, to='sark.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('file', models.ImageField(width_field='image_width', height_field='image_height', upload_to='img')),
                ('thumb', models.ImageField(upload_to='img')),
                ('image_height', models.PositiveIntegerField(editable=False, null=True)),
                ('image_width', models.PositiveIntegerField(editable=False, null=True)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RadioShow',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=200, null=True)),
                ('host', models.ForeignKey(to='sark.Agent')),
                ('performances', models.ManyToManyField(to='sark.Performance')),
                ('photos', models.ManyToManyField(to='sark.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('plaintext_link', models.FilePathField(max_length=200, match='.*\\.txt', path='C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/scripts')),
            ],
        ),
        migrations.AddField(
            model_name='radioshow',
            name='script',
            field=models.ForeignKey(to='sark.Script'),
        ),
        migrations.AddField(
            model_name='performance',
            name='photos',
            field=models.ManyToManyField(to='sark.Photo'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='family',
            field=models.ForeignKey(to='sark.InstrumentFamily'),
        ),
        migrations.AddField(
            model_name='agent',
            name='birthplace',
            field=models.ForeignKey(to='sark.Location', null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='role',
            field=models.ForeignKey(to='sark.Role', default=0),
        ),
    ]
