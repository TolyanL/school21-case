from django.shortcuts import render
from django.http import HttpRequest

from users.forms import ProfileSearchForm
from groups.models import Interest


def home(request: HttpRequest):
    return render(
        request,
        "index.html",
        {
            "search_form": ProfileSearchForm(),
            "tags": Interest.objects.all(),
        },
    )
