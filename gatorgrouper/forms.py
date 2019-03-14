"""
This document contains all of the extended forms used for
our custom User
"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """ New user creation form without username """

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

    student_data = forms.FileField(label="Student data CSV file")
    student_preferences = forms.FileField(
        label="Student preferences CSV file", required=False
    )
    numgrp = forms.TypedChoiceField(
        choices=[
            (str(2 ** i), str(2 ** i)) for i in range(1, 5)
        ],  # Restrict choices to powers of 2
        coerce=int,
        label="Number of groups to create",
    )
    preferences_weight = forms.FloatField(
        label="Importance of an unmatched preference", initial=1.1, min_value=1.0
    )
    preferences_weight_match = forms.FloatField(
        label="Importance of a matched preference", initial=1.25, min_value=1.0
    )


class CreateGroupForm(forms.Form):
    """ Form enabling the creation of a group """

    numgrp = forms.IntegerField(
        min_value=2, max_value=25, label="Number of groups to create"
    )
