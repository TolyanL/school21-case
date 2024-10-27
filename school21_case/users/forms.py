from django import forms
from django.apps import apps


class ProfileSearchForm(forms.Form):
    username = forms.CharField(label="Username", max_length=32)
    intersets = forms.ModelMultipleChoiceField(
        label="Interests",
        queryset=apps.get_model("groups.Interest").objects.all(),
        required=False,
    )
