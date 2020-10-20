from django.urls import path
from . import views

app_name = "Minerva_Home"
urlpatterns = [
    path("", views.index, name="index"),
    #path("logged", views.logged, name = "logged" ),
    #path("login", views.login, name = "login"),
    #path("logout",views.logout, name = "logout")

]
