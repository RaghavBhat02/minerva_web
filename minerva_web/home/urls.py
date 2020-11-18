from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("",views.index,name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("<str:class_url>/", views.class_view, name="class"),
]
