from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class ProfileSearchForm(forms.Form):
    query = forms.CharField(
        max_length=32,
        widget=forms.TextInput(
            attrs={
                "class": "form-control input-field",
                "placeholder": "Введите ник пользователя...",
            }
        ),
    )


class LoginForm(forms.Form):
    email = forms.EmailField(label="Электоронная почта", widget=forms.EmailInput)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


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


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [
            "user",
            "created_at",
            "is_active",
            "groups",
            "interests",
            "avatar",
            "friends",
        ]
