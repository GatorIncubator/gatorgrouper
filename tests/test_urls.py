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
        self.user = models.Professor.objects.create_superuser(email="superuser@user.com", password="super")
        self.client.login(email="superuser@user.com", password="super")


    def test_view_profile(self):
        url = reverse('profile')
        assert url == "/profile/"
