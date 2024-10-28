from django.shortcuts import render
from django.http import HttpRequest

from users.forms import ProfileSearchForm


def home(request: HttpRequest):
    return render(request, "index.html", {"form": ProfileSearchForm()})
