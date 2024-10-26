from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


class CustomUserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]
    list_display = ["username", "email", "first_name", "last_name"]
    search_fields = ["username", "email"]
    # filter_horizontal = ["groups", "interests"]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
