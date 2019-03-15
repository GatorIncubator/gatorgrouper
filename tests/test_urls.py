"""This is undocumented"""
from django.urls import reverse
from gatorgrouper import views, models
from django.test.client import Client
from django.test import SimpleTestCase
import pytest

pytestmark = pytest.mark.django_db


class TestUrl:
    def setup(self):
        self.client = Client()
        self.user = models.Professor.objects.create_superuser(
            email="superuser@user.com", password="super"
        )
        self.client.login(email="superuser@user.com", password="super")

    def test_profile_url(self):
        url = reverse("profile")
        assert url == "/profile/"

    def test_register_url(self):
        url = reverse("register")
        assert url == "/register/"

    def test_home_url(self):
        url = reverse("Gatorgrouper-home")
        assert url == "/"

    def test_classes_url(self):
        url = reverse("Gatorgrouper-classes")
        assert url == "/classes/"

    def test_assignments_url(self):
        url = reverse("Gatorgrouper-assignments")
        assert url == "/assignments/"

    def test_survey_url(self):
        url = reverse("Gatorgrouper-survey")
        assert url == "/survey/"

    def test_groupresults_url(self):
        url = reverse("Gatorgrouper-groups")
        assert url == "/group-result/"

    def test_add_students_url(self):
        url = reverse("add-students")
        assert url == "/add-students/"

    def test_create_groups_url(self):
        url = reverse("create-groups")
        assert url == "/create-groups/"
