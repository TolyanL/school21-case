from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


gender_choices = (("male", "Male"), ("female", "Female"))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nickname = models.CharField(unique=True, max_length=32)
    description = models.CharField(max_length=256, null=True)

    name = models.CharField(null=True)
    surname = models.CharField(null=True)
    lastname = models.CharField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=gender_choices)

    avatar = models.ImageField(upload_to="avatars/", null=True)

    nickname_tg = models.CharField(null=True)
    nickname_ds = models.CharField(null=True)
    study_at = models.CharField(null=True)

    interests = models.ManyToManyField("groups.Interest", related_name="related_profiles", blank=True)
    groups = models.ManyToManyField("groups.Group", related_name="groups", blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("profile", args=[str(self.nickname)])

    def __str__(self):
        return self.name
