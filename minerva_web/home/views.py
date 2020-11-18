from django.shortcuts import render, reverse
from .models import image
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import Class, Tutor

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
        password = request.POST["password"] #store password and password-confirm
        password_confirm = request.POST["password-confirm"]
        if not password == password_confirm:#check if both entered passwords match
            return render(request, "home/signup.html",{
            "message": "Passwords don't match!" #if they don't match say that they don't match
            })
        email = request.POST["email"] #store email
        if not email.endswith('@umich.edu'):#check if email ends with umich.edu
            return render(request, "home/signup.html",{
            "message": "Please use your UMich email! Your email should end with @umich.edu" #if they don't match say that they don't match
            })
        username = request.POST["username"] #store username
        first_name = request.POST["firstname"] #store first name
        last_name = request.POST["lastname"] #store last name
        user = User.objects.create_user(username, email, password) #create user
        user.first_name = first_name #add first name to user
        user.last_name = last_name #add last name to user
        user.save() #save user
        return HttpResponse("USER CREATED!") #send response (replace this with redirect or rendering the decision page)

    return render(request,"home/signup.html")

def class_view(request, class_url):
    class_page = Class.objects.get(url=class_url)
    tutors = Tutor.objects.get(classes=class_page)
    return render(request, "home/class.html", {
        "class_page": class_page,
        "tutors": tutors
    })
