from django.shortcuts import render
from django.http import HttpRequest
from .forms import ProfileSearchForm


def home(request: HttpRequest):
    return render(request, "index.html", {"form": ProfileSearchForm()})
