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
        """ Overrides the current form by customizing it """

        model = get_user_model()
        fields = ("email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):
    """ Custom userchangeform for custom user """

    # pylint: disable=too-few-public-methods
    class Meta:
        """ Overrides the current form by customizing it """

        model = get_user_model()
        fields = ("email", "first_name", "last_name", "password")


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


class AssignmentForm(forms.ModelForm):
    """ This form overrides the current __init__ method
    used when creating a ModelForm so that a user
    can only access their Classes when adding Assignments"""

    # pylint: disable=too-few-public-methods
    class Meta:
        """ This class is undefined """

        model = Assignment
        fields = ("class_id", "assignment_name", "description")

    def __init__(self, user, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        # pylint: disable=no-member
        self.fields["class_id"].queryset = Semester_Class.objects.filter(
            professor_id=user
        )


class StudentForm(forms.ModelForm):
    """ This form overrides the current __init__ method
    used when creating a ModelForm so that a user can
    only access their Classes when adding students """

    # pylint: disable=too-few-public-methods
    class Meta:
        """ This class is undefined """

        model = Student
        fields = ("class_id", "first_name", "last_name")

    def __init__(self, user, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # pylint: disable=no-member
        self.fields["class_id"].queryset = Semester_Class.objects.filter(
            professor_id=user
        )


class GroupForm(forms.ModelForm):
    """ This form is used to create and retrieve groups.
    It overrides the ModelForm __init__ method and restricts
    access to groups to only the user who made the group"""

    # pylint: disable=too-few-public-methods
    class Meta:
        """ This class is undefined """

        model = Grouped_Student
        fields = ("assignment_id",)

    def __init__(self, user, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        # pylint: disable=no-member
        self.fields["assignment_id"].queryset = Assignment.objects.filter(
            professor_id=user
        )
