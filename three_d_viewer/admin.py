"""
Configuration for the Django admin site
"""

from django.contrib import admin
from models import Category, Sample, Question, Answer

admin.site.register(Category)
admin.site.register(Sample)
admin.site.register(Question)
admin.site.register(Answer)
