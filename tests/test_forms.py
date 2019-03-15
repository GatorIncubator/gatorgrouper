from gatorgrouper.forms import CustomUserCreationForm, CustomUserChangeForm, UploadCSVForm, CreateGroupForm

import pytest
pytestmark = pytest.mark.django_db


class TestCustomUserCreationForm:
    # pylint: disable=too-few-public-methods
    def test_valid_data(self):
        form = CustomUserCreationForm({
            "email": "testuserl@test.com",
            "first_name": "Spencer",
            "last_name": "Huang",
            "password1": "testpassword1",
            "password2": "testpassword1",
        })
        assert form.is_valid() is True


class TestCustomUserChangeForm:
    """undocumented"""
    # pylint: disable=too-few-public-methods
    def test_valid_data(self):
        """undocumented"""
        form = CustomUserChangeForm({
            "email": "testuserl@test.com",
            "first_name": "Spencer",
            "last_name": "Huang",
            "password1": "testpassword1",
            "password2": "testpassword1",
        })
        assert form.is_valid() is True


class TestUploadCSVForm:
    """undocumented"""
    # pylint: disable=too-few-public-methods
    def test_valid_data(self, generate_csv):
        """undocumented"""
        form = UploadCSVForm({
            "file": generate_csv,
            "numgrp": 3,
        })
        assert form.fields['file'].label == "Student data CSV file"
        assert form.fields['numgrp'].label == "Number of groups to create"


class TestCreateGroupForm:
    """undocumented"""
    # pylint: disable=too-few-public-methods
    def test_valid_data(self, generate_csv):
        """undocumented"""
        form = CreateGroupForm({
            "numgrp": 3,
        })
        assert form.fields['numgrp'].label == "Number of groups to create"
