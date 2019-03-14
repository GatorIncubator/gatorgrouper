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
from gatorgrouper.forms import CustomUserCreationForm, UploadCSVForm, CreateGroupForm

pytestmark = pytest.mark.django_db


class TestCustomUserCreationForm:
    def test_valid_data(self):
        form = CustomUserCreationForm({
            "email": "testuserl@test.com",
            "first_name": "Spencer",
            "last_name": "Huang",
            "password1": "testpassword1",
            "password2": "testpassword1",
        })
        assert form.is_valid() is True


class TestUploadCSVForm:
    def test_valid_data(self, generate_csv):
        form = UploadCSVForm({
            "file": generate_csv,
            "numgrp": 3,
        })
        # assert form.is_valid() is True

        assert form.fields['file'].label == "Student data CSV file"
        assert form.fields['numgrp'].label == "Number of groups to create"

class TestCreateGroupForm:
    def test_valid_data(self, generate_csv):
        form = CreateGroupForm({
            "numgrp": 3,
        })
        assert form.fields['numgrp'].label == "Number of groups to create"

class TestView:
    def setup(self):
        self.factory = RequestFactory()
        self.user = models.Professor.objects.create_user(email="normaluser@user.com", password="normal")

    def test_home(self):
        "cover home"
        request = self.factory.get(path='/home')
        response = views.home(request)
        assert response.status_code == 200

    def test_register(self):
        request = self.factory.get(path='/register')
        response = views.register(request)
        assert response.status_code == 200

    def test_register_method(self):
        # need to test form.isvalid()
        request = self.factory.get(path='/register')
        request.method = "POST"
        response = views.register(request)
        assert response.status_code == 200

    def test_uploadcsv(self):
        request = self.factory.get(path='/upload_csv')
        response = views.upload_csv(request)
        assert response.status_code == 200

    def test_uploadcsv_method(self):
        # need to test form.isvalid()
        request = self.factory.get(path='/upload_csv')
        request.method = "POST"
        response = views.upload_csv(request)
        assert response.status_code == 200

    # def test_handle_uploaded_file(self, generate_csv):
    #     responses = views.handle_uploaded_file(generate_csv)
    #     assert responses != [' ']

class TestLoginView():
    # fixtures = ['user.json']

    def setup(self):
        self.user = models.Professor.objects.create_user(email="testuser@user.com", password="testuser")
        # self.response = self.user.login(username='testuser',
                                        # password='testpassword')
        self.client = Client()
        # self.factory = RequestFactory()
        # self.user = models.Professor.objects.create_superuser(email="superuser@user.com", password="super")
        # self.client.login(email="superuser@user.com", password="super")



    def test_survey_test(self):
        self.response = self.client.get('/survey', follow=True)
        assert self.response.status_code == 200

    # def test_survey_views_admin(self):

    #     response = self.user.get('/survey', follow=True)
    #     assert response.status_code == 200
    #     data = {
    #         "title": "Survey"}

    #     response = self.user.post('/survey', data=data, follow=True)
    #     assert response.status_code == 200
    def test_profile_login(self):
        # cover profile
        self.response = self.client.get('/profile', follow=True)
        self.client.login(email="testuser@user.com", password="testuser")
        # request.user = self.user
        # response = views.profile(request)
        assert self.response.status_code == 200
        data = {
            "title": "Profile",
            "all_classes": "classes",
            "all_assignments": "assignment_list",
            "all_students": "students"}
        response = self.client.post('/profile', data=data, follow=True)
        assert response.status_code == 200

    def test_create_classes(self):
        self.response = self.client.get('/classes', follow=True)
        self.client.login(email="testuser@user.com", password="testuser")
        assert self.response.status_code == 200

    def test_assignments_login(self):
        self.response = self.client.get('/assignments', follow=True)
        self.client.login(email="testuser@user.com", password="testuser")
        self.response.method = "POST"
        assert self.response.status_code == 200

    def test_groupresults_views(self):
        self.response = self.client.get('/viewing-groups', follow=True)
        self.client.login(email="testuser@user.com", password="testuser")
        assert self.response.status_code == 200

    def test_add_students(self):
        self.response = self.client.get('/add-students', follow=True)
        self.client.login(email="testuser@user.com", password="testuser")
        assert self.response.status_code == 200

    def test_create_groups(self):
        self.response = self.client.get('/create-groups', follow=True)
        self.client.login(email="testuser@user.com", password="testuser")
        assert self.response.status_code == 200
