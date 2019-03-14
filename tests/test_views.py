"""Testing views"""
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
import pytest
from gatorgrouper import views, models
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from mixer.backend.django import mixer
from django.test.client import Client

pytestmark = pytest.mark.django_db


class TestView:
    def setup(self):
        self.factory = RequestFactory()
        self.user = models.Professor.objects.create_user(email="normaluser@user.com", password="normal")

    def test_home(self):
        request = self.factory.get(path='/home')
        response = views.home(request)
        assert response.status_code == 200

    def test_register(self):
        request = self.factory.get(path='/register')
        response = views.register(request)
        assert response.status_code == 200

    def test_uploadcsv(self):
        request = self.factory.get(path='/upload_csv')
        response = views.upload_csv(request)
        assert response.status_code == 200

class TestLoginView:
    def setup(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = models.Professor.objects.create_superuser(email="superuser@user.com", password="super")

    def test_profile_views(self):
        self.client.login(email="superuser@user.com", password="super")
        request = self.client.get('/profile', follow=True)
        response = views.profile(request)
        assert response.status_code == 200

    def test_assignments_views(self):
        self.client.login(email="superuser@user.com", password="super")
        request = self.client.get('/assignments', follow=True)
        response = views.assignments(request)
        assert response.status_code == 200

    def test_survey_views(self):
        self.client.login(email="superuser@user.com", password="super")
        request = self.client.get('/survey', follow=True)
        response = views.survey(request)
        assert response.status_code == 200

    def test_groupresults_views(self):
        self.client.login(email="superuser@user.com", password="super")
        request = self.client.get('/viewing-groups', follow=True)
        response = views.groupResult(request)
        assert response.status_code == 200
