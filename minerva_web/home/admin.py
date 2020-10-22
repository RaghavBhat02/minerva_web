from django.contrib import admin
from .models import image
# Register your models here.
class image_admin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(image, image_admin)
