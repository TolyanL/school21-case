from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


gender_choices = [("male", "Male"), ("female", "Female")]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nickname = models.CharField(unique=True, max_length=32)
    description = models.CharField(max_length=256, null=True, blank=True)

    name = models.CharField(blank=True, null=True)
    surname = models.CharField(blank=True, null=True)
    lastname = models.CharField(blank=True, null=True)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], blank=True, null=True)
    gender = models.CharField(choices=gender_choices, null=True, blank=True)

    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    nickname_tg = models.CharField(blank=True, null=True)
    nickname_ds = models.CharField(blank=True, null=True)
    study_at = models.CharField(blank=True, null=True)

    interests = models.ManyToManyField("groups.Interest", related_name="related_profiles", blank=True)
    groups = models.ManyToManyField("groups.Group", related_name="groups", blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("profile", args=[str(self.nickname)])

    def __str__(self):
        return self.user.username
