from django.shortcuts import render, reverse
from .models import image
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,"home/index.html", {
        "images":image.objects.all()
    })



def logout_view(request):
    logout(request)
    return render(request, "home/login.html", {
                "message": "Logged Out"
            })


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

def signup_view(request):
    if request.method == "POST": #check if method is post
        password = request.POST["password"] #check if both entered passwords match
        password_confirm = request.POST["password-confirm"]
        if not password == password_confirm:
            return render(request, "home/signup.html",{
            "message": "Passwords don't match!" #if they don't match say that they don't match
            })
        email = request.POST["email"] #check if email ends with umich.edu
        if not email.endswith('@umich.edu'):
            return render(request, "home/signup.html",{
            "message": "Please use your UMich email! Your email should end with @umich.edu" #if they don't match say that they don't match
            })
        username = request.POST["username"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return HttpResponse("USER CREATED!")

    return render(request,"home/signup.html")
