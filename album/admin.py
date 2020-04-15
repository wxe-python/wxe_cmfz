from django.contrib import admin

# Register your models here.
from home import models
admin.site.register(models.Album)
admin.site.register(models.Chapter)