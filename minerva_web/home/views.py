from django.shortcuts import render
from .models import image
# Create your views here.

def index(request):
    return render(request,"home/index.html", {
        "images":image.objects.all()
    })
