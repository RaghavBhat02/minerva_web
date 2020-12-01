from django.shortcuts import render, reverse
from .models import image
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import Class, Tutor
import datetime, json
from django.db import IntegrityError
from .forms import TutorForm

#global variables


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        try:
            Tutor.objects.get(user=request.user)
            tutor = True
        except:
            tutor = False
    else:
        tutor = False
    return render(request,"home/index.html", {
        "classes": Class.objects.all(),
        "tutor_is_there": tutor
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
        tutor_yes = request.POST["tutoryes"] #saves whether they want to be a tutor or not
        try:
            user = User.objects.create_user(username, email, password) #create user

            user.first_name = first_name #add first name to user
            user.last_name = last_name #add last name to user
            user.save() #save user
        except IntegrityError:
            return render(request, "home/signup.html", {
                "message":"A user already exists with that username, please try again! If you think this is a mistake, please contact support at elizaday@umich.edu, and refer them to Error 108."
            })

        login(request, user)
        if tutor_yes == "tutor":
             #login as user
            return render(request, "home/tutor_register.html",{
                "classes": Class.objects.all(),
                "new": "true"
            })

        return HttpResponseRedirect(reverse("home:index"))

    return render(request,"home/signup.html")

def class_view(request, class_url):
    class_page = Class.objects.get(url=class_url) #get class based on url
    tutors = Tutor.objects.filter(classes=class_page) #find the tutors who have this class
    return render(request, "home/class.html", { #render the class page
        "class_page": class_page,
        "tutors": tutors
    })
def tutor_view(request, tutor_id):
    tutor = Tutor.objects.get(id=tutor_id)
    return render(request, "home/tutors.html", {
        "tutor": tutor
    })
def registration_view(request):

    if request.method == "POST":
        rate = request.POST["rate"]
        calendly = request.POST["calendly"]
        if not calendly.startswith('https://'):
            calnedly = "https://" + calendly
        why_GT = request.POST["whyGT"]
        what_fav = request.POST["whatfav"]
        best_spot = request.POST["bestspot"]
        any_interesting = request.POST["anyinteresting"]
        class_array_json = request.POST["classestoadd"]
        new_json = request.POST["true"]
        print("new-json:" + new_json)
        new = json.loads(new_json)
        print(new)
        print("a: " + class_array_json)
        class_list = json.loads(class_array_json)
        print(class_list)
        remove_array = request.POST["classestoremove"]
        print("c: " + remove_array)
        remove_list = json.loads(remove_array)
        print(remove_list)
        if rate.startswith('$'):
            end = len(rate) - 1
            rate = rate[1:end]
        #if request.POST["number"]:
            #number = request.POST["number"]

        if request.user.is_authenticated:
            user_person = request.user
        else:
            return render(request, "home/login.html", {
                "message": "There was an error in your sign up process, please contact support to finish singing up. Error #108"
            })
        if new == True:
            new_tutor = Tutor(user=user_person,first_name=user_person.first_name, last_name=user_person.last_name)
        elif new==False:
            new_tutor = Tutor.objects.get(user=user_person)
        new_tutor.why_GT = why_GT
        new_tutor.what_fav = what_fav
        new_tutor.best_spot = best_spot
        new_tutor.any_interesting = any_interesting
        new_tutor.rate = rate
        new_tutor.last_paid = datetime.date(2000, 11, 22)
        new_tutor.calendly = calendly

        #if request.POST["number"]:
            #new_tutor.phone_number = number
        new_tutor.save()


        for item in remove_list:
            try:
                new_tutor.classes.remove(Class.objects.get(url=item))
                new_tutor.save()
            except:
                pass
        for item in class_list:
            try:
                new_tutor.classes.add(Class.objects.get(url=item))
                new_tutor.save()
            except IntegrityError:
                pass

        new_tutor.save()

        return HttpResponseRedirect(reverse("home:index"))
    if not request.user.is_authenticated:
        return HttpResponse("<h1> This page is not accessible to you. Please sign in. </h1>")
    try:
        tutor = Tutor.objects.get(user=request.user)
    except:
        return HttpResponse("<h1> This page is not accessible to you. Please become a Tutor. </h1>")
    return render(request, "home/tutor_register.html", {
        "tutor_classes": Class.objects.filter(tutors=tutor),
        "tutor": tutor,
        "classes": Class.objects.exclude(tutors=tutor),
        "new":"false"
    })
