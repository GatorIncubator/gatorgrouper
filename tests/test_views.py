"""Testing views"""
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
import pytest
from gatorgrouper import views, models
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from django.contrib.messages.storage.fallback import FallbackStorage
from mixer.backend.django import mixer
from django.test.client import Client

pytestmark = pytest.mark.django_db


class TestView:
    """undocumented"""
    def setup(self):
        """undocumented"""
        self.factory = RequestFactory()
        self.user = models.Professor.objects.create_user(email="normaluser@user.com", password="normal")

    def test_home(self):
        "cover home"
        request = self.factory.get(path='/home')
        response = views.home(request)
        assert response.status_code == 200

    def test_register(self):
        """undocumented"""
        request = self.factory.get(path='/register')
        response = views.register(request)
        assert response.status_code == 200

    def test_register_method(self):
        """undocumented"""
        # need to test form.isvalid()
        request = self.factory.get(path='/register', REQUEST_METHOD="POST")
        # request = self.factory.post()
        # request.POST = {
        #     "email": "testuserl@test.com",
        #     "first_name": "Spencer",
        #     "last_name": "Huang",
        #     "password1": "testpassword1",
        #     "password2": "testpassword1",
        # }
        # messages = FallbackStorage(request)
        response = views.register(request)
        assert response.status_code == 200

    def test_uploadcsv(self):
        """undocumented"""
        request = self.factory.get(path='/upload_csv')
        response = views.upload_csv(request)
        assert response.status_code == 200

    def test_uploadcsv_method(self, generate_csv_file):
        """undocumented"""
        # need to test form.isvalid()
        request = self.factory.get(path='/upload_csv')
        request.method = "POST"
        request.POST = {
            "email": "testuserl@test.com",
            "first_name": "Spencer",
            "last_name": "Huang",
            "password1": "testpassword1",
            "password2": "testpassword1",
        }
        # request.FILES = generate_csv_file
        response = views.upload_csv(request)
        assert response.status_code == 200

    # def test_handle_uploaded_file(self, generate_csv_file):
    #     responses = views.handle_uploaded_file(generate_csv_file)
    #     assert responses != [' ']


class TestLoginView():
    """undocumented"""
    def setup(self):
        """undocumented"""
        self.user = models.Professor.objects.create_user(email="testuser@user.com", password="testuser")
        # self.response = self.user.login(username='testuser',
        # password='testpassword')
        # pylint: disable=W0201
        # self.client = Client()
        self.factory = RequestFactory()
        # self.client.login(email="superuser@user.com", password="super")

    def test_survey_test(self):
        """undocumented"""
        request = self.factory.get('/survey')
        request.user = self.user
        response = views.survey(request)
        assert response.status_code == 200

    def test_profile_login(self):
        """undocumented"""
        # cover profile
        request = self.factory.get('/profile')
        request.user = self.user
        response = views.profile(request)
        assert response.status_code == 200
        # data = {
        #     "title": "Profile",
        #     "all_classes": "classes",
        #     "all_assignments": "assignment_list",
        #     "all_students": "students"}
        # response = self.factory.post('/profile', data=data)
        # assert response.status_code == 200

    def test_create_classes_post(self):
        """undocumented"""
        request = self.factory.post('/classes',data=None)
        request.user = self.user
        # self.response.POST = {
        #     "email": "testuserl@test.com",
        #     "first_name": "Spencer",
        #     "last_name": "Huang",
        #     "password1": "testpassword1",
        #     "password2": "testpassword1",
        # }
        response = views.create_classes(request)
        assert response.status_code == 200

    def test_create_classes_get(self):
        """undocumented"""
        request = self.factory.get('/classes',data=None)
        request.user = self.user
        # self.response.POST = {
        #     "email": "testuserl@test.com",
        #     "first_name": "Spencer",
        #     "last_name": "Huang",
        #     "password1": "testpassword1",
        #     "password2": "testpassword1",
        # }
        response = views.create_classes(request)
        assert response.status_code == 200

    def test_assignments_login_get(self):
        """undocumented"""
        request = self.factory.get('/assignments')
        request.user = self.user
        response = views.assignments(request)
        assert response.status_code == 200

    def test_assignments_login_post(self):
        """undocumented"""
        request = self.factory.post('/assignments')
        request.user = self.user
        response = views.assignments(request)
        assert response.status_code == 200

    def test_assignments_login_post_is_valid(self):
        """undocumented"""
        # obj = mixer.blend("gatorgrouper.Assignment", assignment_id=1, assignment_name="Group Project", description="This is an assignment")
        # class_obj = mixer.blend("gatorgrouper.Semester_Class")
        # testdata = {
        #     "assignment_id": obj.assignment_id,
        #     "class_id": class_obj.class_id,
        #     "assignment_name": "Group Project",
        #     "description": "it's lab one"
        # }
        # request = self.factory.post('/assignments', data=testdata)
        # request.user = self.user
        # response = views.assignments(request)
        # assert response.status_code == 200

    def test_groupresults_views_get(self):
        """undocumented"""
        request = self.factory.get('/viewing-groups')
        request.user = self.user
        response = views.groupResult(request)
        assert response.status_code == 200

    def test_groupresults_views_post(self):
        """undocumented"""
        request = self.factory.post('/viewing-groups')
        request.user = self.user
        response = views.groupResult(request)
        assert response.status_code == 200

    def test_groupresults_views_post_formset(self):
        """undocumented"""
        obj = mixer.blend("gatorgrouper.Assignment", assignment_id=1, assignment_name="Group Project", description="This is an assignment")
        testdata = {"assignment_id": obj.assignment_id}

        request = self.factory.post('/viewing-groups', data=testdata)
        request.user = self.user
        response = views.groupResult(request)
        assert response.status_code == 200

    def test_add_students_get(self):
        """undocumented"""
        request = self.factory.get('/add-students')
        request.user = self.user
        response = views.add_students(request)
        assert response.status_code == 200

    def test_add_students_post(self):
        """undocumented"""
        request = self.factory.post('/add-students')
        request.user = self.user
        response = views.add_students(request)
        assert response.status_code == 200

    def test_create_groups_get(self):
        """undocumented"""
        request = self.factory.get('/create-groups')
        request.user = self.user
        response = views.create_groups(request)
        assert response.status_code == 200

    def test_create_groups_post(self):
        """undocumented"""
        request = self.factory.post('/create-groups')
        request.user = self.user
        response = views.create_groups(request)
        assert response.status_code == 200

    @pytest.mark.xfail
    def test_create_groups_post_is_valid(self):
        """undocumented"""
        obj_assignment = mixer.blend("gatorgrouper.Assignment")
        obj_groupedstudents = mixer.blend("gatorgrouper.Grouped_Student", assignment_id=obj_assignment)
        testdata = {
            "assignment_id": obj_assignment.assignment_id,
            "numgrp": 3
        }
        request = self.factory.post('/create-groups', data=testdata, button="save")
        request.user = self.user
        response = views.create_groups(request)
        assert response.status_code == 200
