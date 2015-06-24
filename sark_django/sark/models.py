from django.db import models

# Create your models here.
# class Reel(models.Model):
#     pass
#
#
class Role(models.Model):
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.role


class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


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
    family = models.ForeignKey(InstrumentFamily)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    zoom = models.IntegerField(default=10)

    def __str__(self):
        return "{0}, {1}".format(self.name, self.country)

class Agent(models.Model):
    name = models.CharField(max_length=200)
    primary_place_of_activity = models.ForeignKey(Location, null=True, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    deathdate = models.DateField(blank=True, null=True)
    dates_active = models.CharField(blank=True, null=True, max_length=20)
    bio = models.CharField(default="No bio on record", max_length=2000)
    role = models.ForeignKey(Role, default=0)
    members = models.ManyToManyField("self", blank=True)
    # photos = models.ManyToManyField(Photo)

    def __str__(self):
        return "{} ({})".format(self.name, self.role.role)


class Script(models.Model):
    plaintext_link = models.FilePathField(
        path="C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/scripts",
        match=r".*\.txt",
        max_length=200)
    # tei_link = models.FilePathField(
    #     path="C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/scripts",
    #     match=r".*\.tei",
    #     max_length=200)

    def __str__(self):
        return self.plaintext_link


class Audio(models.Model):
    access_link = models.FilePathField(
        path="C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/audio",
        match=r".*\.mp3",
        max_length=200,
        default=0
    )

    def __str__(self):
        return self.access_link

    class Meta:
        verbose_name_plural = "audio"

class Photo(models.Model):
    file = models.ImageField(upload_to="img", height_field='image_height', width_field='image_width')
    thumb = models.ImageField(upload_to="img")
    image_height = models.PositiveIntegerField(null=True, editable=False)
    image_width = models.PositiveIntegerField(null=True, editable=False)
    description = models.CharField(blank=True, null=True, max_length=300)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.file.name


class Performance(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(null=True)

    audio = models.ForeignKey(Audio)
    location = models.ForeignKey(Location, null=True)
    instruments = models.ManyToManyField(Instrument, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    performers = models.ManyToManyField(Agent, blank=True)
    photos = models.ManyToManyField(Photo)

    def __str__(self):
        return "{0} - {1}".format(self.title, str(self.date))


class RadioShow(models.Model):
    date = models.DateField()
    host = models.ForeignKey(Agent)
    script = models.ForeignKey(Script)
    description = models.CharField(max_length=200, null=True)
    performances = models.ManyToManyField(Performance)
    photos = models.ManyToManyField(Photo)

    def __str__(self):
        return "MTiA: {0} ({1})".format(str(self.date), self.host.name)
