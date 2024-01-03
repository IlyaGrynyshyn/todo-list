from django.contrib import admin
from mainapp.models import Task, Tag

admin.site.register(Task),
admin.site.register(Tag)
