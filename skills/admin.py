from django.contrib import admin
from .models import Category, Skill, Resource, StudySession

admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Resource)
admin.site.register(StudySession)