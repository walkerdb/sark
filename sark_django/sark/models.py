import datetime

from django.db import models


class TimestampedModel(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Role(models.Model):
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.role

    class Meta:
        ordering = ('role',)


class Genre(models.Model):
    genre = models.CharField(max_length=50)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.genre

    class Meta:
        ordering = ('genre',)


class CopyrightStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "copyright statuses"

class InstrumentFamily(models.Model):
    family = models.CharField(max_length=100)

    def __str__(self):
        return self.family

    class Meta:
        verbose_name_plural = "instrument families"

class Instrument(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    family = models.ForeignKey(InstrumentFamily)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Location(TimestampedModel):
    name = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    zoom = models.IntegerField(default=10)

    def __str__(self):
        if self.name:
            return "{0}, {1}".format(self.name, self.country)
        else:
            return self.country

    class Meta:
        ordering = ('country', 'name')

class Image(TimestampedModel):
    file = models.ImageField(upload_to="img", height_field='image_height', width_field='image_width')
    thumb = models.ImageField(upload_to="img")
    image_height = models.PositiveIntegerField(null=True, editable=False)
    image_width = models.PositiveIntegerField(null=True, editable=False)
    description = models.CharField(blank=True, null=True, max_length=300)
    date = models.DateField(blank=True, null=True)
    sort_order = models.IntegerField(default=2)

    def __str__(self):
        return self.file.name

    class Meta:
        ordering = ('date', 'sort_order',)


class Agent(TimestampedModel):
    name = models.CharField(max_length=200)
    primary_place_of_activity = models.ForeignKey(Location, null=True, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    deathdate = models.DateField(blank=True, null=True)
    dates_active = models.CharField(blank=True, null=True, max_length=20)
    bio = models.CharField(default="No bio on record", max_length=2000)
    role = models.ForeignKey(Role, default=0)
    members = models.ManyToManyField("self", blank=True)
    photos = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Performance(TimestampedModel):
    title = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)

    audio = models.FileField(upload_to="audio", null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    instruments = models.ManyToManyField(Instrument, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    performers = models.ManyToManyField(Agent, blank=True)
    photos = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.title, str(self.date))

    class Meta:
        ordering = ('date', 'title')

class Reel(TimestampedModel):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    date = models.DateField(blank=True)
    performances = models.ManyToManyField(Performance)
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class RadioShow(Reel):
    host = models.ForeignKey(Agent)
    script = models.TextField(blank=True)

    class Meta:
        ordering = ('date',)

class FieldRecording(Reel):
    unique_id = models.BigIntegerField()
    recording_engineer = models.ForeignKey(Agent, blank=True)
    location = models.ForeignKey(Location, blank=True)
