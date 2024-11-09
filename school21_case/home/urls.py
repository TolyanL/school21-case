from django.urls import path
from .views import home, about, help_

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("help", help_, name="help"),
]
