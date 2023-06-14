from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.products)
admin.site.register(models.feedback)