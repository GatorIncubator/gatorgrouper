"""
This document contains all of the extended forms used for
our custom User
"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


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
