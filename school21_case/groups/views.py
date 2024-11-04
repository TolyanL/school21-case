from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from .models import Group, Interest
from .forms import CreateGroupForm, GroupSearchForm, GroupEditForm

from users.forms import ProfileSearchForm


@login_required
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


@login_required
def find_groups(request: HttpRequest):
    if request.method == "POST":
        form = GroupSearchForm(request.POST)
        search_query = form.data

        name = search_query.get("group_name")
        interests = search_query.get("interests")

        groups = Group.objects.filter(name__icontains=name)

        if interests:
            groups = groups.filter(tags__id__in=interests).distinct()

        return render(
            request,
            "groups/find_groups.html",
            context={
                "groups": groups.all(),
                "search_form": ProfileSearchForm(),
                "find_group_form": form,
                "search_query": name,
            },
        )

    return render(
        request,
        "groups/find_groups.html",
        {
            "search_form": ProfileSearchForm(),
            "find_group_form": GroupSearchForm(),
            "just_loaded": True,
        },
    )


class GroupDetailView(DetailView):
    model = Group
    template_name = "groups/group_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ProfileSearchForm()
        return context


@login_required
def create_group(request: HttpRequest):
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if not form.errors:
            # print(form.data)
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()

            tags = request.POST.getlist("interests[]")

            # print(request.FILES)

            group.tags.set(tags)
            group.members.add(request.user)
            # print(request.FILES)
            icon = request.FILES.get("icon")
            banner = request.FILES.get("banner")

            if icon:
                group.icon = icon

            if banner:
                group.banner = banner

            if len(tags):
                group.save()
                return redirect("my_groups")
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


@login_required
def edit_group(request: HttpRequest, pk: int):
    group = Group.objects.get(pk=pk)

    if not group or request.user != group.created_by:
        return redirect("my_groups")

    if request.method == "POST":
        form = GroupEditForm(request.POST, instance=group, use_required_attribute=False)

        if not form.errors:
            # print(form.data)
            instance = form.save(commit=False)
            tags = request.POST.getlist("tags[]")

            # print(request.FILES)

            if len(tags):
                instance.tags.set(tags)

            icon = request.FILES.get("icon")
            banner = request.FILES.get("banner")

            if icon:
                instance.icon = icon
            if banner:
                instance.banner = banner

            if len(instance.tags.all()) and not form.errors:
                instance.save()
                return redirect("group_detail", pk=pk)
            form.add_error(None, "Please add at least one interest")

        return render(
            request,
            "groups/edit_group.html",
            {
                "search_form": ProfileSearchForm(),
                "editable": form,
                "group": group,
                "tags": Interest.objects.all(),
            },
        )

    return render(
        request,
        "groups/edit_group.html",
        {
            "search_form": ProfileSearchForm(),
            "editable": GroupEditForm(use_required_attribute=False, instance=group),
            "group": group,
            "tags": Interest.objects.all(),
        },
    )
