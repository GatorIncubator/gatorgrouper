"""Testing views"""
from django.test import RequestFactory
from django.contrib.messages.storage.fallback import FallbackStorage

# from django.core.files.uploadedfile import SimpleUploadedFile
import pytest
from mixer.backend.django import mixer
from gatorgrouper import views, models

pytestmark = pytest.mark.django_db


class TestView:
    """undocumented"""

    def setup(self):
        """undocumented"""
        # pylint: disable=W0201
        self.factory = RequestFactory()
        self.user = models.Professor.objects.create_user(
            email="normaluser@user.com", password="normal"
        )

    def test_home(self):
        "cover home"
        request = self.factory.get(path="/home")
        response = views.home(request)
        assert response.status_code == 200

    def test_register(self):
        """undocumented"""
        request = self.factory.get(path="/register")
        response = views.register(request)
        assert response.status_code == 200

    def test_register_method(self):
        """undocumented"""
        testdata = {
            "email": "testuserl@test.com",
            "first_name": "Spencer",
            "last_name": "Huang",
            "password1": "testpassword1",
            "password2": "testpassword1",
        }
        request = self.factory.post("/register", data=testdata)
        setattr(request, "session", "ssession")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        # request = self.factory.post("/register", data=testdata, messages=messages)
        response = views.register(request)
        assert response.status_code == 302

    def test_uploadcsv(self):
        """undocumented"""
        request = self.factory.get(path="/upload_csv")
        response = views.upload_csv(request)
        assert response.status_code == 200

    def test_uploadcsv_post(self, generate_csv_file):
        """undocumented"""

        # with open(generate_csv_file) as f:
        # request = self.factory.post("/upload_csv")
        # request = self.factory.post("/upload_csv",
        # f=SimpleUploadedFile(f.read(), b"file_content"))
        f = generate_csv_file.open()
        request = self.factory.post("/upload_csv", {"file": f})
        # request.FILES["file"] = f.read()
        # request.FILES["file"] = f.read()
        # request.FILES['file'].read()
        setattr(request, "session", "ssession")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        response = views.upload_csv(request)
        assert response.status_code == 200

    # pylint: disable=R0201
    def test_handle_uploaded_file(self, generate_csv_file):
        """undocumented"""
        responses = views.handle_uploaded_file(generate_csv_file.open())
        assert responses != [" "]


class TestLoginView:
    """undocumented"""

    def setup(self):
        """undocumented"""
        # pylint: disable=W0201
        self.user = models.Professor.objects.create_user(
            email="testuser@user.com", password="testuser"
        )
        self.factory = RequestFactory()

    def test_survey_test(self):
        """undocumented"""
        request = self.factory.get("/survey")
        request.user = self.user
        response = views.survey(request)
        assert response.status_code == 200

    def test_profile_login(self):
        """undocumented"""
        # cover profile
        request = self.factory.get("/profile")
        request.user = self.user
        response = views.profile(request)
        assert response.status_code == 200

    def test_create_classes_post(self):
        """undocumented"""
        prof_obj = mixer.blend("gatorgrouper.Professor")
        obj = mixer.blend(
            "gatorgrouper.Semester_Class",
            professor_id=prof_obj,
            semester="S19",
            department="CS",
            class_number="CS101",
            class_section="01",
        )
        testdata = {
            "professor_id": prof_obj.professor_id,
            "class_id": obj.class_id,
            "semester": "S19",
            "department": "CS",
            "class_number": "CS101",
            "class_section": "01",
        }
        request = self.factory.post("/classes", data=testdata)
        request.user = self.user
        setattr(request, "session", "ssession")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        response = views.create_classes(request)
        assert response.status_code == 302

    def test_create_classes_get(self):
        """undocumented"""
        request = self.factory.get("/classes")
        request.user = self.user
        response = views.create_classes(request)
        assert response.status_code == 200

    def test_assignments_login_get(self):
        """undocumented"""
        request = self.factory.get("/assignments")
        request.user = self.user
        response = views.assignments(request)
        assert response.status_code == 200

    def test_assignments_login_post(self):
        """undocumented"""
        request = self.factory.post("/assignments")
        request.user = self.user
        response = views.assignments(request)
        assert response.status_code == 200

    def test_assignments_login_post_is_valid(self):
        """undocumented"""
        obj = mixer.blend(
            "gatorgrouper.Assignment",
            assignment_id=1,
            assignment_name="Group Project",
            description="This is an assignment",
        )
        class_obj = mixer.blend("gatorgrouper.Semester_Class")
        testdata = {
            "assignment_id": obj.assignment_id,
            "class_id": class_obj.class_id,
            "assignment_name": "Group Project",
            "description": "it's lab one",
        }
        request = self.factory.post("/assignments", data=testdata)
        setattr(request, "session", "ssession")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        # response = views.create_classes(request)
        request.user = self.user
        response = views.assignments(request)
        assert response.status_code == 200

    def test_assignment_view(self):
        """undocumented"""

        mixer.blend("gatorgrouper.Assignment")
        request = self.factory.get("/assignment/1/")
        request.user = self.user
        response = views.AssignmentView.as_view()(request, pk=1)
        assert response.status_code == 200

    def test_add_students_get(self):
        """undocumented"""
        request = self.factory.get("/add-students")
        request.user = self.user
        response = views.add_students(request)
        assert response.status_code == 200

    def test_add_students_post(self):
        """undocumented"""
        mixer.blend("gatorgrouper.Student", first_name="test", last_name="user")
        class_obj = mixer.blend("gatorgrouper.Semester_Class")
        testdata = {
            "class_id": class_obj.class_id,
            "first_name": "test",
            "last_name": "user",
        }
        request = self.factory.post("/add-students", data=testdata)
        request.user = self.user
        setattr(request, "session", "ssession")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        response = views.add_students(request)
        assert response.status_code == 200

    def test_create_groups_get(self):
        """undocumented"""
        request = self.factory.get("/create-groups")
        request.user = self.user
        response = views.create_groups(request)
        assert response.status_code == 200

    def test_create_groups_post(self):
        """undocumented"""
        request = self.factory.post("/create-groups")
        request.user = self.user
        response = views.create_groups(request)
        assert response.status_code == 200

    # @pytest.mark.xfail
    def test_create_groups_post_is_valid(self):
        """undocumented"""
        obj_assignment = mixer.blend("gatorgrouper.Assignment")
        # obj_groupedstudents = mixer.blend(
        #     "gatorgrouper.Grouped_Student", assignment_id=obj_assignment
        # )
        testdata = {"assignment_id": obj_assignment.assignment_id, "numgrp": 3}
        request = self.factory.post("/create-groups", data=testdata, button="save")
        request.user = self.user
        response = views.create_groups(request)
        assert response.status_code == 200
