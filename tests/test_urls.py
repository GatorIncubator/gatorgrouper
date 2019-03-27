"""This is undocumented"""
from django.urls import reverse
from django.test.client import Client
import pytest
from mixer.backend.django import mixer
from gatorgrouper import models

pytestmark = pytest.mark.django_db


class TestUrl:
    """undocumented"""

    def setup(self):
        """undocumented"""
        # pylint: disable=W0201
        self.client = Client()
        self.user = models.Professor.objects.create_superuser(
            email="superuser@user.com", password="super"
        )
        self.client.login(email="superuser@user.com", password="super")

    # pylint: disable=R0201
    def test_profile_url(self):
        """undocumented"""
        url = reverse("profile")
        assert url == "/profile/"

    # pylint: disable=R0201
    def test_register_url(self):
        """undocumented"""
        url = reverse("register")
        assert url == "/register/"

    # pylint: disable=R0201
    def test_home_url(self):
        """undocumented"""
        url = reverse("Gatorgrouper-home")
        assert url == "/"

    # pylint: disable=R0201
    def test_classes_url(self):
        """undocumented"""
        url = reverse("Gatorgrouper-classes")
        assert url == "/classes/"

    # pylint: disable=R0201
    def test_assignments_url(self):
        """undocumented"""
        url = reverse("Gatorgrouper-assignments")
        assert url == "/assignments/"

    # pylint: disable=R0201
    def test_survey_url(self):
        """undocumented"""
        url = reverse("Gatorgrouper-survey")
        assert url == "/survey/"

    # pylint: disable=R0201
    def test_assignmentview_url(self):
        """undocumented"""
        obj = mixer.blend("gatorgrouper.Assignment")
        url = reverse("assignment-detail", args=(obj.pk,))
        assert url == "/assignment/1/"

    # pylint: disable=R0201
    def test_add_students_url(self):
        """undocumented"""
        url = reverse("add-students")
        assert url == "/add-students/"

    # pylint: disable=R0201
    def test_create_groups_url(self):
        """undocumented"""
        url = reverse("create-groups")
        assert url == "/create-groups/"
