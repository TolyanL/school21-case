from django.shortcuts import render, redirect
from django.http import HttpRequest

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from .forms import ProfileSearchForm, LoginForm, RegistrationForm


def profile(request: HttpRequest, username: str):
    return render(request, "profile.html", {"username": username})


def search_profile(request: HttpRequest):
    search_query = ProfileSearchForm(request.POST)

    if request.method == "POST" and search_query.is_valid():
        search_query = search_query.cleaned_data

        if not request.user.is_authenticated:
            return redirect("sign_up")

        nickname = search_query.get("nickname")
        interests = search_query.get("interests")

        profile = User.objects.filter(profile__nickname__icontains=nickname)

        if interests:
            profile = profile.filter(profile__interests__id__in=interests).distinct()

        if profile:
            return render(
                request,
                "user_search.html",
                context={
                    "users": profile.all(),
                    "search_form": ProfileSearchForm(),
                    "search_query": nickname,
                },
            )

    return redirect("home")


def sign_up(request: HttpRequest):
    search_form = ProfileSearchForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user_item = User.objects.filter(email=email).first()

            if user_item:
                user = authenticate(request, username=user_item.username, password=password)
                if user:
                    login(request, user)
                    return redirect("home")

    return render(request, "users/login.html", {"login_form": LoginForm(), "search_form": search_form})


def register(request: HttpRequest):
    search_form = ProfileSearchForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if not form.errors:
            exist_item = User.objects.filter(email=form.cleaned_data["email"]).first()

            if not exist_item:
                data = form.cleaned_data

                form.save()
                user = authenticate(request, username=data["username"], password=data["password1"])

                login(request, user)
                return redirect("home")

            form.add_error("email", "User with this email already exists")

        return render(request, "users/register.html", {"reg_form": form, "search_form": search_form})

    form = RegistrationForm()
    return render(request, "users/register.html", {"reg_form": form, "search_form": search_form})


def user_logout(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    return redirect("sign_up")


def my_profile(request: HttpRequest):
    return render(request, "users/profile.html", {"user": request.user, "search_form": ProfileSearchForm()})


def edit_profile(request: HttpRequest):
    return render(request, "profile_edit.html")
