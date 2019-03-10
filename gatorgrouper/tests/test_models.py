"""models.py testing"""

import pytest
from mixer.backend.django import mixer
# from models import Professor
from django.contrib.auth import get_user_model


pytestmark = pytest.mark.django_db


class Test_UserManager:
    """test UserManager class"""

    # @classmethod
    # def test_create_user(self):
    #     """undocumented"""
    #     Professor.objects.create_user(email="test@test.test",
    #                                   password="testpassword")
    #     user = Professor.objects.get(email="test@test.test")
    #     assert user.is_superuser is False
    # assert user == ""

    # @classmethod
    # def test_create_superuser(self):
    #     """undocumented"""
    #     Professor.objects.create_superuser(email="test@test.test",
    #                                        password="testpassword")
    #     user = Professor.objects.get(email="test@test.test")
    #     assert user.is_superuser is False

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normaluser@user.com', password='normal')
        assert user.email == 'normaluser@user.com'
        assert user.is_superuser is False

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(email='superuser@user.com', password='super')
        assert user.is_staff is True
        assert user.is_superuser is True

    def test_is_superuser_exception(self):
        with pytest.raises(ValueError):
            User = get_user_model()
            User.objects.create_superuser(email='superuser@user.com', password='super', is_superuser=False)

    def test_is_staff_exception(self):
        with pytest.raises(ValueError):
            User = get_user_model()
            User.objects.create_superuser(email='superuser@user.com', password='super', is_staff=False)

    def test_email_exception(self):
        with pytest.raises(ValueError):
            User = get_user_model()
            User.objects._create_user(email=None, password='super', is_superuser=False)


class Test_Professor:
    """test professor class"""

    # pylint: disable=R0201
    # def test_model(self):
    #     """test professor model by creating a professor instance and assert
    #     that there is one in the database"""
    #     Professor.objects.create_user(email="test@test.test",
    #                                   password="testpassword")
    # it creates a professor instance
    #     assert Professor.pk == 1

    # pylint: disable=R0201
    def test_str(self):
        """test __str__ method by putting varibles into the database and
        expecting the output to be in a specific format"""
        obj = mixer.blend("gatorgrouper.Professor", last_name="K", first_name="Greg")
        result = str(obj)
        expected = "K, Greg"
        assert result == expected


class Test_Semester_Class:
    """test semester class"""

    # pylint: disable=R0201
    def test_model(self):
        """test semester model by creating a semester and class instance and
        assert that there is one in the database"""
        obj = mixer.blend("gatorgrouper.Semester_Class")
        # it creates a semester class instance
        assert obj.pk == 1

    # pylint: disable=R0201
    def test_str(self):
        """test __str__ method by putting varibles into the database and
        expecting the output to be in a specific format"""
        obj = mixer.blend(
            "gatorgrouper.Semester_Class",
            department="CS",
            class_number="203",
            class_section="01",
        )
        result = str(obj)
        expected = "CS: 203*01"
        assert result == expected


class Test_Assignments:
    """test assignment class"""

    # pylint: disable=R0201
    def test_model(self):
        """test assignment model by creating a assignment instance and asserted
        that database is not empty"""
        obj = mixer.blend("gatorgrouper.Assignment")
        # it creates a assignment instance
        assert obj.pk != " "

    # pylint: disable=R0201
    def test_str(self):
        """test __str__ method by putting varibles into the database and
        expecting the output to be in a specific format"""
        obj = mixer.blend("gatorgrouper.Assignment", assignment_id="Assignment One")
        result = str(obj)
        expected = "Assignment One"
        assert result == expected


class Test_Student:
    """test student class"""

    # pylint: disable=R0201
    def test_model(self):
        """test student model by creating a student instance and assert that
        there is one in the database"""
        obj = mixer.blend("gatorgrouper.Student")
        # it creates a student instance
        assert obj.pk == 1

    # pylint: disable=R0201
    def test_str(self):
        """test __str__ method by putting varibles into the database and
        expecting the output to be in a specific format"""
        obj = mixer.blend("gatorgrouper.Student", last_name="Y", first_name="Enpu")
        result = str(obj)
        expected = "Y, Enpu"
        assert result == expected


class Test_Grouped_Student:
    """test grouped student class"""

    # pylint: disable=R0201
    def test_model(self):
        """test grouped student model by creating a grouped student instance and
        assert that there is one in the database"""
        obj = mixer.blend("gatorgrouper.Grouped_Student")
        # it creates a grouped students instance
        assert obj.pk == 1

    # pylint: disable=R0201
    def test_str(self):
        """test __str__ method """
        obj = mixer.blend("gatorgrouper.Grouped_Student")
        result = str(obj)
        expectedsymbol = ":"
        assert expectedsymbol in result
