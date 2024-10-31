from django.urls import path
from .views import my_groups

urlpatterns = [
    path("my-groups", my_groups, name="my_groups"),

]
