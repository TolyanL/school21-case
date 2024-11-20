from django.urls import path
from .views import (
    add_friend,
    my_profile,
    edit_profile,
    remove_friend,
    remove_list_friend,
    search_profile,
    sign_up,
    register,
    user_logout,
    confirm_2fa,
    ProfileDetailView,
    FriendsListView,
)

urlpatterns = [
    path("profile/detail/<int:pk>", ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/search/", search_profile, name="profile_search"),
    path("my-profile/", my_profile, name="my_profile"),
    path("my-profile/edit", edit_profile, name="profile_edit"),
    path("friends/<int:pk>", FriendsListView.as_view(), name="friends_list"),
    path("add-friend/<int:pk>", add_friend, name="add_friend"),
    path("remove-friend/<int:pk>", remove_friend, name="remove_friend"),
    path("remove-list-friend/<int:pk>", remove_list_friend, name="remove_lfriend"),
    path("login/", sign_up, name="sign_up"),
    path("verify/", confirm_2fa, name="confirm_2fa"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
]
