from django.shortcuts import render, reverse
from .models import image
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request,"home/index.html", {
        "images":image.objects.all()
    })



def logout_view(request):
     pass
     # Pass is a simple way to tell python to do nothing.

    # Additional imports we'll need:


def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("home:index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "home/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "home/login.html")
