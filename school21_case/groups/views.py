from django.shortcuts import render
from django.http import HttpRequest


def my_groups(request: HttpRequest):
    return render(request, "groups/my_groups.html")