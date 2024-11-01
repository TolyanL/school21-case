from django.shortcuts import render, redirect
from django.http import HttpRequest

from .models import Interest
from .forms import CreateGroupForm

from users.forms import ProfileSearchForm


def my_groups(request: HttpRequest):
    user = request.user
    return render(
        request,
        "groups/my_groups.html",
        {
            "search_form": ProfileSearchForm(),
            "groups": user.group_members.all(),
        },
    )


def find_groups(request: HttpRequest):
    return render(request, "groups/find_groups.html", {"search_form": ProfileSearchForm()})


def create_group(request: HttpRequest):
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if not form.errors:
            # print(form.data)
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()

            tags = request.POST.getlist("interests[]")

            # print(request.FILES.get("icon"))
            # print(form.is_multipart())

            group.tags.set(tags)
            group.members.add(request.user)

            if request.FILES.get("icon"):
                group.icon = request.FILES.get("icon")

            if len(tags):
                group.save()
                return redirect("my_profile")
            group.delete()
            form.add_error(None, "Please add at least one interest")

    return render(
        request,
        "groups/create_group.html",
        {
            "search_form": ProfileSearchForm(),
            "create_form": CreateGroupForm(),
            "interests": Interest.objects.all(),
        },
    )
