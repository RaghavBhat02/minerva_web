from django.contrib import admin
from .models import image
# Register your models here.
class image_admin(admin.ModelAdmin):
    list_display = ("id", "name")
"""class admin_Class(admin.ModelAdmin):
    list_display = ("department", "number")
class admin_Tutor(admin.ModelAdmin):"""

admin.site.register(image, image_admin)
#admin.site.register(Class, admin_Class)
#admin.site.register(Tutor, adminTutor)
