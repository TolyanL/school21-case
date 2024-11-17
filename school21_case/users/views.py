from random import randint

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.db.models import Q
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.generic import DetailView

from school21_case.settings import EMAIL_HOST_USER

from .forms import ProfileSearchForm, LoginForm, RegistrationForm, ProfileEditForm
from groups.models import Interest


class ProfileDetailView(DetailView):
    model = User
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ProfileSearchForm()
        context["tags"] = Interest.objects.all()
        return context


@login_required
def search_profile(request: HttpRequest):
    search_query_raw = ProfileSearchForm(request.POST)

    if request.method == "POST" and search_query_raw.is_valid():
        search_query = search_query_raw.cleaned_data

        query = search_query.get("query")
        tags = search_query_raw.data.getlist("tags[]")

        profile = User.objects.filter(
            Q(profile__nickname__icontains=query)
            | Q(profile__name__icontains=query)
            | Q(profile__surname__icontains=query)
            | Q(profile__lastname__icontains=query)
        )

        if tags:
            profile = profile.filter(profile__interests__id__in=tags).distinct()

        return render(
            request,
            "users/user_search.html",
            context={
                "users": profile.all(),
                "search_form": ProfileSearchForm(),
                "tags": Interest.objects.all(),
                "search_query": query,
            },
        )
    return render(
        request,
        "users/user_search.html",
        context={"search_form": ProfileSearchForm(), "tags": Interest.objects.all()},
    )


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
                    otp = randint(1000, 999999)
                    request.session["otp"] = otp
                    request.session["email"] = email
                    send_mail(
                        "Ваш код двухфакторной аутенфикации",
                        f"Код: {otp}",
                        EMAIL_HOST_USER,
                        [user.email],
                        fail_silently=False,
                    )
                    return redirect("confirm_2fa")

    return render(
        request,
        "users/login.html",
        {
            "login_form": LoginForm(),
            "search_form": search_form,
            "tags": Interest.objects.all(),
        },
    )


def confirm_2fa(request: HttpRequest):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")

        if entered_otp == str(request.session.get("otp")):
            user = User.objects.filter(email=request.session.get("email")).first()
            login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "users/confirm_2fa.html",
                {
                    "search_form": ProfileSearchForm(),
                    "tags": Interest.objects.all(),
                    "email": request.session.get("email"),
                    "error": "Не верный код",
                },
            )

    return render(
        request,
        "users/confirm_2fa.html",
        {
            "search_form": ProfileSearchForm(),
            "tags": Interest.objects.all(),
            "email": request.session.get("email"),
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
            instance = form.save(commit=False)
            tags = request.POST.getlist("interests[]")

            if 0 < len(tags) <= 5:
                instance.interests.set(tags)
            else:
                form.add_error(None, "Вы можете выбрать не более 5 интересов.")

            if request.FILES.get("avatar"):
                profile.avatar = request.FILES.get("avatar")
                profile.save()

            if not form.errors:
                instance.save()
                return redirect("my_profile")

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
