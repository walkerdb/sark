from django.contrib import admin
from . import models as m

@admin.register(m.RadioShow)
class RadioShowAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'


@admin.register(m.Performance)
class PerformanceAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'

@admin.register(m.Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(m.Audio)
class AudioAdmin(admin.ModelAdmin):
    pass

@admin.register(m.CopyrightStatus)
class CopyrightAdmin(admin.ModelAdmin):
    pass

@admin.register(m.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(m.Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(m.Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    pass

@admin.register(m.InstrumentFamily)
class InstrumentFamilyAdmin(admin.ModelAdmin):
    pass

@admin.register(m.Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(m.Script)
class ScriptAdmin(admin.ModelAdmin):
    pass

@admin.register(m.Role)
class RoleAdmin(admin.ModelAdmin):
    pass