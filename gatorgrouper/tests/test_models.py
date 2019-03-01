"""models.py testing"""

import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestProfessor:
    """test professor class"""
    # pylint: disable=R0201
    def test_model(self):
        """test professor model by creating a professor instance and assert
        that there is one in the database"""
        obj = mixer.blend('gatorgrouper.Professor')
        # it creates a professor instance
        assert obj.pk == 1

    # pylint: disable=R0201
    def test_str(self):
        """test __str__ method by putting varibles into the database and
        expecting the output to be in a specific format"""
        obj = mixer.blend('gatorgrouper.Professor', last_name='K', first_name='Greg')
        result = obj.__str__()
        expected = 'K, Greg'
        assert result == expected


class TestSemesterClss:
    """test semester class"""
    # pylint: disable=R0201
    def test_model(self):
        """test semester model"""
        obj = mixer.blend('gatorgrouper.Semester_Class')
        # it creates a semester class instance
        assert obj.pk == 1

    # pylint: disable=R0201
    def test_str(self):
        """test __str__ method """
        obj = mixer.blend('gatorgrouper.Semester_Class',
                          department='CS', class_number='203', class_section='01')
        result = obj.__str__()
        expected = 'CS: 203*01'
        assert result == expected


class TestAssignments:
    """test assignment class"""
    # pylint: disable=R0201
    def test_model(self):
        """test assignment model"""
        obj = mixer.blend('gatorgrouper.Assignments')
        # it creates a assignment instance
        assert obj.pk != " "

    # pylint: disable=R0201
    def test_str(self):
        """test __str__ method """
        obj = mixer.blend('gatorgrouper.Assignments', assignment_id='Assignment One')
        result = obj.__str__()
        expected = 'Assignment One'
        assert result == expected


class TestStudents:
    """test student class"""
    # pylint: disable=R0201
    def test_model(self):
        """test student model"""
        obj = mixer.blend('gatorgrouper.Students')
        # it creates a student instance
        assert obj.pk == 1

    # pylint: disable=R0201
    def test_str(self):
        """test __str__ method """
        obj = mixer.blend('gatorgrouper.Students', last_name='Y', first_name='Enpu')
        result = obj.__str__()
        expected = 'Y, Enpu'
        assert result == expected


class TestGrouped_Students:
    """test grouped student class"""
    # pylint: disable=R0201
    def test_model(self):
        """test grouped student model"""
        obj = mixer.blend('gatorgrouper.Grouped_Students')
        # it creates a grouped students instance
        assert obj.pk == 1

    # pylint: disable=R0201
    def test_str(self):
        """test __str__ method """
        obj = mixer.blend('gatorgrouper.Grouped_Students')
        result = obj.__str__()
        assert str(obj) == result
