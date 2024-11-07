from django import forms
from .models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "description"]


class GroupSearchForm(forms.Form):
    group_name = forms.CharField(
        max_length=32,
        widget=forms.TextInput(
            attrs={
                "class": "form-control input-field",
                "placeholder": "Введите название группы...",
            }
        ),
    )


class GroupEditForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "description"]
