# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('name', models.CharField(max_length=200)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('deathdate', models.DateField(blank=True, null=True)),
                ('dates_active', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.CharField(max_length=2000, default='No bio on record')),
                ('members', models.ManyToManyField(blank=True, to='sark.Agent', related_name='members_rel_+')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CopyrightStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'copyright statuses',
            },
        ),
        migrations.CreateModel(
            name='FieldRecording',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField(blank=True)),
                ('unique_id', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('genre', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ('genre',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('file', models.ImageField(height_field='image_height', upload_to='img', width_field='image_width')),
                ('thumb', models.ImageField(upload_to='img')),
                ('image_height', models.PositiveIntegerField(editable=False, null=True)),
                ('image_width', models.PositiveIntegerField(editable=False, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('sort_order', models.IntegerField(default=2)),
            ],
            options={
                'ordering': ('date', 'sort_order'),
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='InstrumentFamily',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('family', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'instrument families',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('name', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('zoom', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ('country', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('audio', models.FileField(null=True, upload_to='audio')),
                ('genres', models.ManyToManyField(blank=True, to='sark.Genre')),
                ('instruments', models.ManyToManyField(blank=True, to='sark.Instrument')),
                ('location', models.ForeignKey(to='sark.Location', blank=True, null=True)),
                ('performers', models.ManyToManyField(blank=True, to='sark.Agent')),
                ('photos', models.ManyToManyField(blank=True, to='sark.Image')),
            ],
            options={
                'ordering': ('date', 'title'),
            },
        ),
        migrations.CreateModel(
            name='RadioShow',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2015, 7, 16, 2, 57, 50, 364900))),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField(blank=True)),
                ('script', models.TextField(blank=True)),
                ('host', models.ForeignKey(to='sark.Agent')),
                ('images', models.ManyToManyField(blank=True, to='sark.Image')),
                ('performances', models.ManyToManyField(to='sark.Performance')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('role', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('role',),
            },
        ),
        migrations.AddField(
            model_name='instrument',
            name='family',
            field=models.ForeignKey(to='sark.InstrumentFamily'),
        ),
        migrations.AddField(
            model_name='fieldrecording',
            name='images',
            field=models.ManyToManyField(blank=True, to='sark.Image'),
        ),
        migrations.AddField(
            model_name='fieldrecording',
            name='location',
            field=models.ForeignKey(blank=True, to='sark.Location'),
        ),
        migrations.AddField(
            model_name='fieldrecording',
            name='performances',
            field=models.ManyToManyField(to='sark.Performance'),
        ),
        migrations.AddField(
            model_name='fieldrecording',
            name='recording_engineer',
            field=models.ForeignKey(blank=True, to='sark.Agent'),
        ),
        migrations.AddField(
            model_name='agent',
            name='photos',
            field=models.ManyToManyField(blank=True, to='sark.Image'),
        ),
        migrations.AddField(
            model_name='agent',
            name='primary_place_of_activity',
            field=models.ForeignKey(to='sark.Location', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='role',
            field=models.ForeignKey(to='sark.Role', default=0),
        ),
    ]
