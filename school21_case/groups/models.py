from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=256, null=True)
    logo = models.ImageField(upload_to="group_logos/", null=True)

    # members = models.ManyToManyField("users.Profile", related_name="group_members", blank=True)
    # created_by = models.ForeignKey("users.Profile", on_delete=models.CASCADE, related_name="groups_created")

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
