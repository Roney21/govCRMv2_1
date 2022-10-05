from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class UserForm(forms.Form):
    name = forms.FileField()


class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ["email", "password"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
