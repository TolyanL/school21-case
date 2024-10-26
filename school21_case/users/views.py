from django.shortcuts import render
from django.http import HttpRequest


def profile(request: HttpRequest, username: str):
    return render(request, "profile.html", {"username": username})


def my_profile(request: HttpRequest):
    return render(request, "profile.html", {"username": "User_Profile"})


def edit_profile(request: HttpRequest):
    return render(request, "profile_edit.html")
