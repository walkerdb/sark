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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('deathdate', models.DateField(null=True, blank=True)),
                ('dates_active', models.CharField(max_length=20, null=True, blank=True)),
                ('bio', models.CharField(default='No bio on record', max_length=2000)),
                ('members', models.ManyToManyField(related_name='members_rel_+', blank=True, to='sark.Agent')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CopyrightStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'copyright statuses',
            },
        ),
        migrations.CreateModel(
            name='FieldRecording',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=50)),
                ('description', models.TextField(default='', blank=True)),
            ],
            options={
                'ordering': ('genre',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(height_field='image_height', width_field='image_width', upload_to='img')),
                ('thumb', models.ImageField(upload_to='img')),
                ('image_height', models.PositiveIntegerField(editable=False, null=True)),
                ('image_width', models.PositiveIntegerField(editable=False, null=True)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('sort_order', models.IntegerField(default=2)),
            ],
            options={
                'ordering': ('date', 'sort_order'),
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='', blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='InstrumentFamily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('family', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'instrument families',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('country', models.CharField(max_length=50)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('zoom', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ('country', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(null=True, blank=True)),
                ('audio', models.FileField(null=True, upload_to='audio')),
                ('genres', models.ManyToManyField(to='sark.Genre', blank=True)),
                ('instruments', models.ManyToManyField(to='sark.Instrument', blank=True)),
                ('location', models.ForeignKey(to='sark.Location', null=True, blank=True)),
                ('performers', models.ManyToManyField(to='sark.Agent', blank=True)),
                ('photos', models.ManyToManyField(to='sark.Image', blank=True)),
            ],
            options={
                'ordering': ('date', 'title'),
            },
        ),
        migrations.CreateModel(
            name='RadioShow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('date', models.DateField(blank=True)),
                ('script', models.TextField(blank=True)),
                ('host', models.ForeignKey(to='sark.Agent')),
                ('images', models.ManyToManyField(to='sark.Image', blank=True)),
                ('performances', models.ManyToManyField(to='sark.Performance')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            field=models.ManyToManyField(to='sark.Image', blank=True),
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
            field=models.ManyToManyField(to='sark.Image', blank=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='primary_place_of_activity',
            field=models.ForeignKey(to='sark.Location', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='role',
            field=models.ForeignKey(default=0, to='sark.Role'),
        ),
    ]
