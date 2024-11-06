from django.urls import path
from .views import (
    my_profile,
    edit_profile,
    search_profile,
    sign_up,
    register,
    user_logout,
    confirm_2fa,
    ProfileDetailView,
)

urlpatterns = [
    path("profile/detail/<int:pk>", ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/search/", search_profile, name="profile_search"),
    path("my-profile/", my_profile, name="my_profile"),
    path("my-profile/edit", edit_profile, name="profile_edit"),
    path("login/", sign_up, name="sign_up"),
    path("verify/", confirm_2fa, name="confirm_2fa"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
]
