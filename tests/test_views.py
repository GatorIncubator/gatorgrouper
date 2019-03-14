"""Testing views"""
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
import pytest
from gatorgrouper import views, models
from django.http import HttpRequest
from django.test import TestCase
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

    def test_register_method(self):
        request = self.factory.get(path='/register')
        request.method = "POST"
        response = views.register(request)
        assert response.status_code == 200

    def test_uploadcsv(self):
        request = self.factory.get(path='/upload_csv')
        response = views.upload_csv(request)
        assert response.status_code == 200

    def test_uploadcsv_method(self):
        request = self.factory.get(path='/upload_csv')
        request.method = "POST"
        response = views.upload_csv(request)
        assert response.status_code == 200

    # def test_handle_uploaded_file(self, generate_csv):
    #     responses = views.handle_uploaded_file(generate_csv)
    #     assert responses != [' ']

class TestLoginView:
    fixtures = ['user.json']

    def setup(self):
        self.client = Client()
        self.response = self.client.login(username='testuser',
                                          password='testpassword')
        # self.client = Client()
        # self.factory = RequestFactory()
        # self.user = models.Professor.objects.create_superuser(email="superuser@user.com", password="super")
        # self.client.login(email="superuser@user.com", password="super")

    def test_profile_views(self):
        self.response = self.client.get('/profile', follow=True)
        # request.user = self.user
        # response = views.profile(request)
        assert self.response.status_code == 200

    def test_assignments_views(self):
        request = self.client.get('/assignments', follow=True)
        request.user = self.user
        request.method = "POST"
        response = views.assignments(request)
        assert response.status_code == 200

    def test_survey_views(self):
        request = self.client.get('/survey', follow=True)
        response = views.survey(request)
        assert response.status_code == 200

    def test_groupresults_views(self):
        request = self.client.get('/viewing-groups', follow=True)
        response = views.groupResult(request)
        assert response.status_code == 200

    def test_create_classes(self):
        request = self.client.get('/classes', follow=True)
        response = views.create_classes(request)
        assert response.status_code == 200

    def test_add_students(self):
        request = self.client.get('/add-students', follow=True)
        response = views.add_students(request)
        assert response.status_code == 200

    def test_create_groups(self):
        request = self.client.get('/create-groups', follow=True)
        request.method == "POST"
        response = views.create_groups(request)
        assert response.status_code == 200
