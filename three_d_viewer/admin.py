"""
Configuration for the Django admin site
"""

from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from three_d_viewer.models import Category, Sample, Question, Answer, Mineral, GlossaryEntry

admin.site.register(Category)
admin.site.register(Sample)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Mineral)
#admin.site.register(GlossaryEntry)


class GlossaryEntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(GlossaryEntry, GlossaryEntryAdmin)