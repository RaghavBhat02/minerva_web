from django.db import models

# Create your models here.
class image(models.Model):
    image = models.ImageField(upload_to = 'home/images', blank = False)
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"
