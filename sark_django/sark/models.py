from django.db import models

# Create your models here.
# class Reel(models.Model):
#     pass
#
#
class Role(models.Model):
    role = models.CharField(max_length=200)


class Location(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    zoom = models.IntegerField(default=10)


class CopyrightStatus(models.Model):
    status = models.CharField(max_length=50)


class Person(models.Model):
    name = models.CharField(max_length=200)
    birthplace = models.ForeignKey(Location, null=True)
    birthdate = models.DateField(blank=True, null=True)
    deathdate = models.DateField(blank=True, null=True)
    bio = models.CharField(default="No bio on record", max_length=2000)
    role = models.ForeignKey(Role, default=0)
    # photos = models.ManyToManyField(Photo)


class Script(models.Model):
    plaintext_link = models.FilePathField(
        path="C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/scripts",
        match=r".*\.txt",
        max_length=200)
    # tei_link = models.FilePathField(
    #     path="C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/scripts",
    #     match=r".*\.tei",
    #     max_length=200)


class Audio(models.Model):
    access_link = models.FilePathField(
        path="C:/Users/dev/PycharmProjects/sark_django/sark_django/static/sarkfiles/audio",
        match=r".*\.mp3",
        max_length=200,
        default=0
    )

class RadioShow(models.Model):
    date = models.DateField()
    host = models.ForeignKey(Person)
    script = models.ForeignKey(Script)
    audio = models.ForeignKey(Audio)
    # performances = models.ManyToManyField(Performance)




# class Performance(models.Model):
#     title = models.CharField(max_length=200)
#     location = models.ForeignKey(Location, null=True)
#     date = models.DateField()
#
#     # instruments = models.ManyToManyField(Instrument)
#     # genres = models.ManyToManyField(Genre)
#     performers = models.ManyToManyField(Person, null=True)
#     # groups = models.ManyToManyField(Group, null=True)


# class Group(models.Model):
#     members = models.ManyToManyField(Person)
#     name = models.CharField(max_length=100)


# class InstrumentFamily(models.Model):
#     family = models.CharField(max_length=100)


# class Instrument(models.Model):
#     name = models.CharField(max_length=100)
#     family = models.ForeignKey(InstrumentFamily)



#
# class Photo(models.Model):
#     filename = models.FileField()
#     description = models.CharField()
#     date = models.DateField(blank=True)
