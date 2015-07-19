import re

from django.contrib import admin
from django import forms
from . import models as m


class ApproximateDateForm(forms.ModelForm):
    class Meta:
        model = m.FieldRecording
        fields = ('title', 'description', 'unique_id', 'location', 'recording_engineer', 'date_text', 'date_accuracy', 'performances', 'images')

    def clean(self):
        format_regex = r'[12][90]\d\d\-[01]\d\-[0-3]\d|[12][90]\d\d\-[01]\d|[12][90]\d\d'
        alpha_regex = r'[a-z][A-Z]'
        date_text = self.cleaned_data.get('date_text')
        if not re.match(format_regex, date_text) or re.match(alpha_regex, date_text) or date_text.endswith("-"):
            raise forms.ValidationError("Please enter date text in the format 'yyyy-mm-dd', up to the point of highest certainty (eg '1965', '1965-02', or '1965-02-24')")
        return self.cleaned_data


@admin.register(m.RadioShow)
class RadioShowAdmin(admin.ModelAdmin):
    fields = ('title', 'type', 'description', 'host', 'date', 'script', 'performances', 'images')
    date_hierarchy = 'date'
    filter_horizontal = ('images', 'performances')

@admin.register(m.FieldRecording)
class FieldRecordingAdmin(admin.ModelAdmin):
    form = ApproximateDateForm
    date_hierarchy = 'date'
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

@admin.register(m.DateApproximationLevel)
class DateApproximationAdmin(admin.ModelAdmin):
    pass