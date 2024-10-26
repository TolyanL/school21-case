from django.contrib import admin
from .models import Group, Interest


class GroupAdmin(admin.ModelAdmin):
    list_display = ["name", "created_by", "created_at", "hide"]
    search_fields = ["name"]
    filter_horizontal = ["tags", "members"]


admin.site.register(Group, GroupAdmin)
admin.site.register(Interest)
