from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Professor
        fields = ("email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Professor
        fields = ("email", "first_name", "last_name")


class UploadCSVForm(forms.Form):
    """ Form enabling the uploading of a CSV file to be used for grouping """

    file = forms.FileField(label="Student data CSV file")
    numgrp = forms.IntegerField(
        min_value=2, max_value=25, label="Number of groups to create"
    )
