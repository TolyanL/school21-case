from django.urls import path
from .views import my_groups, find_groups

urlpatterns = [
    path("my-groups", my_groups, name="my_groups"),
    path("find-groups", find_groups, name="find_groups"),
]
