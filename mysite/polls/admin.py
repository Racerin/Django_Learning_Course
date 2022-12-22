from django.contrib import admin

from .models import Question, Choice

# Register your models here.

# Add the feature in admin webpage to create 'question' object.
admin.site.register(Question)
admin.site.register(Choice)