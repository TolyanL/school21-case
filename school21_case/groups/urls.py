from django.urls import path
from .views import my_groups, find_groups, create_group, group_detail

urlpatterns = [
    path("my-groups", my_groups, name="my_groups"),
    path("group/<int:group_id>", group_detail, name="group_detail"),
    path("find-groups", find_groups, name="find_groups"),
    path("create-group", create_group, name="create_group"),
]
