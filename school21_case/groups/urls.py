from django.urls import path
from .views import my_groups, create_group


urlpatterns = [
    path("my-groups", my_groups, name="my_groups"),
    path("create-group", create_group, name="create_group"),

]
