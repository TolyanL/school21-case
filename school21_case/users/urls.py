from django.urls import path
from .views import profile, my_profile, edit_profile, search_profile, sign_up, register_profile

urlpatterns = [
    path("profile/<str:username>", profile),
    path("profile/search/", search_profile, name="profile_search"),
    path("my-profile/", my_profile, name="my_profile"),
    path("my-profile/edit", edit_profile, name="profile_edit"),
    path("login/", sign_up, name="sign_up"),
    path("register/", register_profile, name="register"),
]
