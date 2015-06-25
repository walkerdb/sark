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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('deathdate', models.DateField(null=True, blank=True)),
                ('dates_active', models.CharField(null=True, max_length=20, blank=True)),
                ('bio', models.CharField(max_length=2000, default='No bio on record')),
                ('members', models.ManyToManyField(related_name='members_rel_+', blank=True, to='sark.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('access_link', models.FilePathField(max_length=200, match='.*\\.mp3', default=0, path='C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/audio')),
            ],
            options={
                'verbose_name_plural': 'audio',
            },
        ),
        migrations.CreateModel(
            name='CopyrightStatus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'copyright statuses',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('file', models.ImageField(width_field='image_width', upload_to='img', height_field='image_height')),
                ('thumb', models.ImageField(upload_to='img')),
                ('image_height', models.PositiveIntegerField(null=True, editable=False)),
                ('image_width', models.PositiveIntegerField(null=True, editable=False)),
                ('description', models.CharField(null=True, max_length=300, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentFamily',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('family', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'instrument families',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(null=True)),
                ('audio', models.ForeignKey(to='sark.Audio')),
                ('genres', models.ManyToManyField(blank=True, to='sark.Genre')),
                ('instruments', models.ManyToManyField(blank=True, to='sark.Instrument')),
                ('location', models.ForeignKey(null=True, to='sark.Location')),
                ('performers', models.ManyToManyField(blank=True, to='sark.Agent')),
                ('photos', models.ManyToManyField(to='sark.Image')),
            ],
        ),
        migrations.CreateModel(
            name='RadioShow',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(null=True, max_length=200)),
                ('host', models.ForeignKey(to='sark.Agent')),
                ('performances', models.ManyToManyField(to='sark.Performance')),
                ('photos', models.ManyToManyField(to='sark.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('plaintext_link', models.FilePathField(max_length=200, match='.*\\.txt', path='C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/scripts')),
            ],
        ),
        migrations.AddField(
            model_name='radioshow',
            name='script',
            field=models.ForeignKey(to='sark.Script'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='family',
            field=models.ForeignKey(to='sark.InstrumentFamily'),
        ),
        migrations.AddField(
            model_name='agent',
            name='primary_place_of_activity',
            field=models.ForeignKey(null=True, blank=True, to='sark.Location'),
        ),
        migrations.AddField(
            model_name='agent',
            name='role',
            field=models.ForeignKey(to='sark.Role', default=0),
        ),
    ]
