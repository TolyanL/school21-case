from django.contrib.admin.templatetags.admin_list import search_form
from django.shortcuts import render
from django.http import HttpRequest
from users.forms import ProfileSearchForm

def my_groups(request: HttpRequest):
    return render(request, "groups/my_groups.html", {"search_form": ProfileSearchForm()})

def find_groups(request: HttpRequest):
    return render(request, "groups/find_groups.html", {"search_form": ProfileSearchForm()})

def create_group(request: HttpRequest):
    return render(request, "groups/create_group.html")
    
