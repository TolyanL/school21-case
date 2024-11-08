from django.urls import path
from .views import (
    delete_group,
    my_groups,
    find_groups,
    create_group,
    GroupDetailView,
    GroupMembers,
    edit_group,
    join_group,
    leave_group,
)

urlpatterns = [
    path("my-groups", my_groups, name="my_groups"),
    path("detail/<int:pk>", GroupDetailView.as_view(), name="group_detail"),
    path("detail/<int:pk>/members", GroupMembers.as_view(), name="group_members"),
    path("edit/<int:pk>", edit_group, name="edit_group"),
    path("delete/<int:pk>", delete_group, name="delete_group"),
    path("join/<int:pk>", join_group, name="join_group"),
    path("leave/<int:pk>", leave_group, name="leave_group"),
    path("find-groups", find_groups, name="find_groups"),
    path("create-group", create_group, name="create_group"),
]
