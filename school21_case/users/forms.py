from django import forms

# from django.apps import apps
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class ProfileSearchForm(forms.Form):
    nickname = forms.CharField(
        max_length=32,
        widget=forms.TextInput(
            attrs={
                "class": "form-control input-field",
                "placeholder": "Enter nickname...",
            }
        ),
    )
    # intersets = forms.ModelMultipleChoiceField(
    #     label="Interests",
    #     queryset=apps.get_model("groups.Interest").objects.all(),
    #     required=False,
    # )


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username"]

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
            profile = Profile(user=user, nickname=self.cleaned_data["username"])
            profile.save()

        return user
