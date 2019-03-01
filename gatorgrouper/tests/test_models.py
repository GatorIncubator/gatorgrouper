"""models.py testing"""

import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestProfessor:
    """test professor class"""
    def test_model(self):
        obj = mixer.blend('gatorgrouper.Professor')
        # it creates a professor instance
        assert obj.pk == 1

    def test_str(self):
        obj = mixer.blend('gatorgrouper.Professor', last_name='K', first_name='Greg')
        result = obj.__str__()
        expected = 'K, Greg'
        assert result == expected

class TestSemesterClss:
    """test semester class"""
    def test_model(self):
        obj = mixer.blend('gatorgrouper.Semester_Class')
        # it creates a semester class instance
        assert obj.pk == 1

    def test_str(self):
        obj = mixer.blend('gatorgrouper.Semester_Class',
                          department='CS', class_number='203', class_section='01')
        result = obj.__str__()
        expected = 'CS: 203*01'
        assert result == expected

class TestAssignments:
    """test semester class"""
    def test_model(self):
        obj = mixer.blend('gatorgrouper.Assignments')
        # it creates a assignment instance
        assert obj.pk != " "

    def test_str(self):
        obj = mixer.blend('gatorgrouper.Assignments', assignment_id='Assignment One')
        result = obj.__str__()
        expected = 'Assignment One'
        assert result == expected

class TestStudents:
    """test student class"""
    def test_model(self):
        obj = mixer.blend('gatorgrouper.Students')
        # it creates a student instance
        assert obj.pk == 1

    def test_str(self):
        obj = mixer.blend('gatorgrouper.Students', last_name='Y', first_name='Enpu')
        result = obj.__str__()
        expected = 'Y, Enpu'
        assert result == expected

class TestGrouped_Students:
    """test grouped student class"""
    def test_model(self):
        obj = mixer.blend('gatorgrouper.Grouped_Students')
        # it creates a grouped students instance
        assert obj.pk == 1

    def test_str(self):
        obj = mixer.blend('gatorgrouper.Grouped_Students')
        result = obj.__str__()
        assert str(obj) == result
