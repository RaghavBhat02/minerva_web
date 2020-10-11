from django.urls import path
from . import views

app_name = "Minerva_Home"
urlpatterns = [
    path("", views.index, name="index")
]
