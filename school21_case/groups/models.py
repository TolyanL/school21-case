from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="Название")
    description = models.CharField(max_length=256, null=True, verbose_name="Описание")

    icon = models.ImageField(upload_to="group_icons/", null=True)
    banner = models.ImageField(upload_to="group_banners/", null=True)

    members = models.ManyToManyField(User, related_name="group_members", blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="groups_created")

    hide = models.BooleanField(default=False)
    tags = models.ManyToManyField("Interest", related_name="related_groups")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
