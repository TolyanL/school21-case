from django.shortcuts import render
from django.http import HttpRequest
from django.db.models import Count

from users.forms import ProfileSearchForm
from groups.models import Interest, Group


def home(request: HttpRequest):
    groups = Group.objects.annotate(num_members=Count("members")).order_by("-num_members").all()
    return render(
        request,
        "index.html",
        {
            "search_form": ProfileSearchForm(),
            "tags": Interest.objects.all(),
            "groups": groups,
        },
    )
