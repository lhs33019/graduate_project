from django.contrib import admin
from .models import WeightFile, ImageFile

# Register your models here.
admin.site.register(WeightFile)
admin.site.register(ImageFile)