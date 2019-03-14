"""Testing views"""
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
import pytest
from gatorgrouper import views, models
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestHomeView:
    def setup(self):
        self.factory = RequestFactory()
        self.user = models.Professor.objects.create_user(email="normaluser@user.com", password="normal")

    def test_home(self):
        request = self.factory.get(path='/home')
        response = views.home(request)
        assert response.status_code == 200
