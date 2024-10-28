from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User

from .forms import ProfileSearchForm, LoginForm, RegistrationForm


def profile(request: HttpRequest, username: str):
    return render(request, "profile.html", {"username": username})


def search_profile(request: HttpRequest):
    search_query = ProfileSearchForm(request.POST)

    if request.method == "POST" and search_query.is_valid():
        search_query = search_query.cleaned_data

        username = search_query.get("username")
        interests = search_query.get("interests")

        profile = User.objects.filter(profile__nickname__icontains=username)

        if interests:
            profile = profile.filter(profile__interests__id__in=interests).distinct()

        if profile:
            return render(request, "user_search.html", context={"users": profile.all()})

    return redirect("home")


def sign_up(request: HttpRequest):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if not form.errors:
            print(form.is_valid)
            print(form.errors)
            print(form.cleaned_data)
            form.save()
            return redirect("home")
        print(form.errors)
        return render(request, "register.html", {"reg_form": form})

    form = RegistrationForm()
    return render(request, "register.html", {"reg_form": form})


def register_profile(request: HttpRequest):
    pass


def my_profile(request: HttpRequest, username: str):
    return render(request, "profile.html", {"profile": 0})


def edit_profile(request: HttpRequest):
    return render(request, "profile_edit.html")
