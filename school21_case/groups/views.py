from django.shortcuts import render
from django.http import HttpRequest


def my_groups(request: HttpRequest):
    return render(request, "groups/my_groups.html")


def create_group(request: HttpRequest):
    return render(request, "groups/create_group.html")
    