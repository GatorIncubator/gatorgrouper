"""
This document contains all of the extended forms used for
our custom User
"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Assignment, Semester_Class, Student, Grouped_Student


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

    file = forms.FileField(label="Student data CSV file")
    numgrp = forms.IntegerField(
        min_value=2, max_value=25, label="Number of groups to create"
    )


class CreateGroupForm(forms.Form):
    """ Form enabling the creation of a group """

    numgrp = forms.IntegerField(
        min_value=2, max_value=25, label="Number of groups to create"
    )



class AssignmentForm(forms.ModelForm):
    """ This form overrides the current __init__ method
    used when creating a ModelForm so that a user
    can only access their Classes when adding Assignments"""

    class Meta:
        model = Assignment
        fields = ("class_id", "assignment_name", "description")

    def __init__(self, user, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.fields['class_id'].queryset = Semester_Class.objects.filter(professor_id=user)
class GroupForm(forms.ModelForm):
    """ This form is used to create and retrieve groups.
    It overrides the ModelForm __init__ method and restricts
    access to groups to only the user who made the group"""

    class Meta:
        model = Grouped_Student
        fields = ("assignment_id", )
    def __init__(self, user, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['assignment_id'].queryset = Assignment.objects.filter(professor_id=user)
