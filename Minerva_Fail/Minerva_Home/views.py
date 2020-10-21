from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def index (request):
    return render(request,"Minerva_Home/index.html")

def logged(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "Minerva_Home/logged.html")

def login_view(request):

    return render(request, "Minerva_Home/login.html")

# logs out user
def logout_view(request):
    logout(request)
    return render(request, "Minerva_Home/login.html", {
                "message": "Logged Out"
            })
"""
if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return HttpResponseRedirect(reverse("logged"))
    else:
        return render(request, "Minerva_Home/login.html", {
            "message": "Invalid Credentials"
        })

"""
