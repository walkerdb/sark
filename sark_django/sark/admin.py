from django.contrib import admin
from . import models as m

@admin.register(m.RadioShow)
class RadioShowAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'host', 'date', 'script', 'performances', 'images')
    date_hierarchy = 'date'
    filter_horizontal = ('images', 'performances')

@admin.register(m.FieldRecording)
class FieldRecordingAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'unique_id', 'location', 'recording_engineer', 'date', 'performances', 'images')
    filter_horizontal = ('images', 'performances')

@admin.register(m.Performance)
class PerformanceAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    filter_horizontal = ('instruments', 'genres', 'performers', 'photos')

@admin.register(m.Agent)
class AgentAdmin(admin.ModelAdmin):
    filter_horizontal = ('members', 'photos')

@admin.register(m.CopyrightStatus)
class CopyrightAdmin(admin.ModelAdmin):
    pass

@admin.register(m.Genre)
class GenreAdmin(admin.ModelAdmin):
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


@admin.register(m.Role)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(m.Image)
class ImageAdmin(admin.ModelAdmin):
    pass