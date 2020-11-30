from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class image(models.Model):
    image = models.ImageField(upload_to = 'home/images', blank = False)
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"

class Class(models.Model):
    department = models.CharField(max_length=32)
    number = models.IntegerField()
    url = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=64, blank=True)


    def __str__(self):
        return f"{self.department} {self.number}"

class Tutor(models.Model):
    user = models.ForeignKey(User,blank=False, null=False,on_delete=models.CASCADE, related_name = "tutor")
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    last_paid = models.DateField()
    phone_number = models.IntegerField(null=True)
    why_GT = models.CharField(max_length=300)
    what_fav = models.TextField()
    best_spot = models.TextField()
    any_interesting = models.TextField()
    classes = models.ManyToManyField(Class, blank=True, related_name="tutors")
    profile_pic = models.ImageField(upload_to= 'home/static/images')
    rate = models.FloatField()
    rating = models.FloatField(null=True)
    calendly = models.TextField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.rating}"
