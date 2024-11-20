from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User

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
            "tags": Interest.objects.all(),
            "groups": user.group_members.all(),
        },
    )


@login_required
def find_groups(request: HttpRequest):
    if request.method == "POST":
        form = GroupSearchForm(request.POST)
        search_query = form.data

        name = search_query.get("group_name")
        tags = search_query.get("interests[]")

        groups = Group.objects.filter(name__icontains=name)

        if tags:
            groups = groups.filter(tags__id__in=tags).distinct()

        return render(
            request,
            "groups/find_groups.html",
            context={
                "groups": groups.all(),
                "tags": Interest.objects.all(),
                "search_form": ProfileSearchForm(),
                "find_group_form": form,
                "search_query": name,
            },
        )

    groups = Group.objects.annotate(num_members=Count("members")).order_by("-num_members").all()
    return render(
        request,
        "groups/find_groups.html",
        {
            "search_form": ProfileSearchForm(),
            "tags": Interest.objects.all(),
            "find_group_form": GroupSearchForm(),
            "just_loaded": True,
            "groups": groups,
        },
    )


class GroupDetailView(DetailView):
    model = Group
    template_name = "groups/group_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ProfileSearchForm()
        context["tags"] = Interest.objects.all()
        return context


class GroupMembers(ListView):
    model = User
    template_name = "groups/group_members.html"
    context_object_name = "members"
    paginate_by = 6

    def get_queryset(self):
        group_id = self.kwargs.get("pk")
        return User.objects.filter(group_members=group_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = ProfileSearchForm()
        context["tags"] = Interest.objects.all()
        context["group_pk"] = self.kwargs.get("pk")
        return context


@login_required
def create_group(request: HttpRequest):
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if not form.errors:
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()

            tags = request.POST.getlist("interests[]")

            group.tags.set(tags)
            group.members.add(request.user)
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
            "tags": Interest.objects.all(),
            "create_form": CreateGroupForm(),
        },
    )


@login_required
def edit_group(request: HttpRequest, pk: int):
    group = get_object_or_404(Group, pk=pk)

    if not group or request.user != group.created_by:
        return redirect("my_groups")

    if request.method == "POST":
        form = GroupEditForm(request.POST, instance=group, use_required_attribute=False)

        if not form.errors:
            instance = form.save(commit=False)
            tags = request.POST.getlist("tags[]")

            if len(tags):
                if len(tags) > 5:
                    form.add_error(None, "Вы можете добавить не более 5 интересов.")
                else:
                    instance.tags.set(tags)
            else:
                form.add_error(None, "Добавьте хотя бы один интерес.")

            icon = request.FILES.get("icon")
            banner = request.FILES.get("banner")

            if icon:
                instance.icon = icon
            if banner:
                instance.banner = banner

            if not form.errors:
                instance.save()
                return redirect("group_detail", pk=pk)

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


@login_required
def delete_group(request: HttpRequest, pk: int):
    group = Group.objects.get(pk=pk)

    if not group or request.user != group.created_by:
        return redirect("group_detail", pk=pk)

    if request.method == "POST":
        if request.POST.get("yes"):
            group.delete()
            return redirect("my_groups")
        return redirect("group_detail", pk=pk)

    return render(
        request,
        "groups/delete_group.html",
        {
            "search_form": ProfileSearchForm(),
            "tags": Interest.objects.all(),
            "group": group,
        },
    )


@login_required
def join_group(request: HttpRequest, pk: int):
    group = get_object_or_404(Group, pk=pk)
    group.members.add(request.user)
    return redirect("group_detail", pk=pk)


@login_required
def leave_group(request: HttpRequest, pk: int):
    group = get_object_or_404(Group, pk=pk)
    group.members.remove(request.user)
    return redirect("group_detail", pk=pk)
