"""
Configuration for the Django admin site
"""

from django.contrib import admin
from three_d_viewer.models import Category, Sample, Question, Answer, Mineral

admin.site.register(Category)
admin.site.register(Sample)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Mineral)
