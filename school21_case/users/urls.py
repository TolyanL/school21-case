from django.urls import path
from .views import profile, my_profile, edit_profile

urlpatterns = [
    path("profile/<str:username>", profile, name="home"),
    path("my-profile/", my_profile, name="my_profile"),
    path("my-profile/edit", edit_profile, name="profile_edit"),
]
