from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("",views.index,name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("profile-edit/", views.registration_view, name="registration"),
    path("tutor/<int:tutor_id>/", views.tutor_view, name="tutor"),
    path("class/<str:class_url>/", views.class_view, name="class"),

]
