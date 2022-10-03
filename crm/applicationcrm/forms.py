from django import forms


class UserForm(forms.Form):
    name = forms.FileField()
    age = forms.IntegerField()