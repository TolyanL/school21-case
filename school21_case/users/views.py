from django.shortcuts import render, redirect
from django.http import HttpRequest

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from .forms import ProfileSearchForm, LoginForm, RegistrationForm, ProfileEditForm
from groups.models import Interest


@login_required
def profile(request: HttpRequest, username: str):
    return render(request, "profile.html", {"username": username})


@login_required
def search_profile(request: HttpRequest):
    search_query_raw = ProfileSearchForm(request.POST)

    if request.method == "POST" and search_query_raw.is_valid():
        search_query = search_query_raw.cleaned_data

        nickname = search_query.get("nickname")
        tags = search_query_raw.data.getlist("tags[]")

        profile = User.objects.filter(profile__nickname__icontains=nickname)

        if tags:
            profile = profile.filter(profile__interests__id__in=tags).distinct()

        if profile:
            return render(
                request,
                "user_search.html",
                context={
                    "users": profile.all(),
                    "search_form": ProfileSearchForm(),
                    "tags": Interest.objects.all(),
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

    return render(
        request,
        "users/login.html",
        {
            "login_form": LoginForm(),
            "search_form": search_form,
            "tags": Interest.objects.all(),
        },
    )


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
    return render(
        request,
        "users/register.html",
        {
            "reg_form": form,
            "search_form": search_form,
            "tags": Interest.objects.all(),
        },
    )


def user_logout(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    return redirect("sign_up")


@login_required
def my_profile(request: HttpRequest):
    return render(
        request,
        "users/profile.html",
        {
            "user": request.user,
            "search_form": ProfileSearchForm(),
            "tags": Interest.objects.all(),
        },
    )


@login_required
def edit_profile(request: HttpRequest):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=profile, use_required_attribute=False)

        if not form.errors:
            # print(form.data)
            instance = form.save(commit=False)
            tags = request.POST.getlist("interests[]")

            # print(request.FILES.get("avatar"))

            if len(tags):
                instance.interests.set(tags)

            if request.FILES.get("avatar"):
                profile.avatar = request.FILES.get("avatar")
                profile.save()

            instance.save()

            return redirect("my_profile")

        # print(form.errors)

        return render(
            request,
            "users/profile_edit.html",
            {
                "search_form": ProfileSearchForm(),
                "editable": form,
                "profile": profile,
                "tags": Interest.objects.all(),
            },
        )

    return render(
        request,
        "users/profile_edit.html",
        {
            "search_form": ProfileSearchForm(),
            "editable": ProfileEditForm(use_required_attribute=False, instance=request.user.profile),
            "profile": request.user.profile,
            "tags": Interest.objects.all(),
        },
    )
