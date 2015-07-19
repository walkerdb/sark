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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('deathdate', models.DateField(null=True, blank=True)),
                ('dates_active', models.CharField(null=True, blank=True, max_length=20)),
                ('bio', models.CharField(default='No bio on record', max_length=2000)),
                ('members', models.ManyToManyField(related_name='members_rel_+', to='sark.Agent', blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CopyrightStatus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'copyright statuses',
            },
        ),
        migrations.CreateModel(
            name='DateApproximationLevel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('approximation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FieldRecording',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('date_text', models.CharField(null=True, blank=True, max_length=25)),
                ('date', models.DateField(blank=True)),
                ('unique_id', models.BigIntegerField()),
                ('date_accuracy', models.ForeignKey(blank=True, null=True, to='sark.DateApproximationLevel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('file', models.ImageField(height_field='image_height', width_field='image_width', upload_to='img')),
                ('thumb', models.ImageField(upload_to='img')),
                ('image_height', models.PositiveIntegerField(null=True, editable=False)),
                ('image_width', models.PositiveIntegerField(null=True, editable=False)),
                ('description', models.CharField(null=True, blank=True, max_length=300)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('family', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'instrument families',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=50)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(null=True, blank=True)),
                ('audio', models.FileField(null=True, upload_to='audio')),
                ('genres', models.ManyToManyField(to='sark.Genre', blank=True)),
                ('instruments', models.ManyToManyField(to='sark.Instrument', blank=True)),
                ('location', models.ForeignKey(blank=True, null=True, to='sark.Location')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('date_text', models.CharField(null=True, blank=True, max_length=25)),
                ('date', models.DateField(blank=True)),
                ('script', models.TextField(blank=True)),
                ('type', models.BooleanField(choices=[(0, 'Insert'), (1, 'Broadcast')], default=1)),
                ('date_accuracy', models.ForeignKey(blank=True, null=True, to='sark.DateApproximationLevel')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
            field=models.ForeignKey(to='sark.Location', blank=True),
        ),
        migrations.AddField(
            model_name='fieldrecording',
            name='performances',
            field=models.ManyToManyField(to='sark.Performance'),
        ),
        migrations.AddField(
            model_name='fieldrecording',
            name='recording_engineer',
            field=models.ForeignKey(to='sark.Agent', blank=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='photos',
            field=models.ManyToManyField(to='sark.Image', blank=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='primary_place_of_activity',
            field=models.ForeignKey(blank=True, null=True, to='sark.Location'),
        ),
        migrations.AddField(
            model_name='agent',
            name='role',
            field=models.ForeignKey(to='sark.Role', default=0),
        ),
    ]
