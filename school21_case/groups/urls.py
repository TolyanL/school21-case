from django.urls import path
from .views import my_groups, find_groups, create_group, GroupDetailView  # group_detail

urlpatterns = [
    path("my-groups", my_groups, name="my_groups"),
    path("detail/<int:pk>", GroupDetailView.as_view(), name="group_detail"),
    path("find-groups", find_groups, name="find_groups"),
    path("create-group", create_group, name="create_group"),
]
