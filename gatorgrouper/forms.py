"""
This document contains all of the extended forms used for
our custom User
"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    """ New user creation form without username """

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        """ This class is undocumented """

        model = get_user_model()
        fields = ("email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):
    """ Custom userchangeform for custom user """

    # pylint: disable=too-few-public-methods
    class Meta:
        """ This class is undocumented """

        model = get_user_model()
        fields = ("email", "first_name", "last_name")


class UploadCSVForm(forms.Form):
    """ Form enabling the uploading of a CSV file to be used for grouping """

    file = forms.FileField(label="Student data CSV file")
    numgrp = forms.IntegerField(
        min_value=2, max_value=25, label="Number of groups to create"
    )
