from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User

from .forms import ProfileSearchForm


def profile(request: HttpRequest, username: str):
    return render(request, "profile.html", {"username": username})


def search_profile(request: HttpRequest):
    form = ProfileSearchForm()

    search_query = ProfileSearchForm(request.POST)

    if request.method == "POST" and search_query.is_valid():
        search_query = search_query.cleaned_data

        username = search_query.get("username")
        interests = search_query.get("interests")

        profile = User.objects.filter(username__icontains=username)

        if interests:
            profile = profile.filter(profile__interests__id__in=interests).distinct()

        if profile:
            return render(request, "profile.html", context={"user": profile.first()})

    return redirect("home", {"form": form})


def my_profile(request: HttpRequest, username: str):
    return render(request, "profile.html", {"profile": 0})


def edit_profile(request: HttpRequest):
    return render(request, "profile_edit.html")
