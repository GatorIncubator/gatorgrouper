"""Test suite for the gatorgrouper.py module"""
import pytest
import parse_gatorgrouper_arguments
import display_student_groups
import remove_absent_students
import sys

def test_check_valid_group_size_one():
    """Checking the group size of one"""
    group_size = 1
    student_identifiers = ['maria', 'dan', 'simon', 'jesse', 'jon', 'michael', 'jacob', 'kapfhammer']
    student_groups = parse_gatorgrouper_arguments.check_valid_group_size(group_size, student_identifiers)
    assert student_groups == False

def test_check_valid_group_size_quarter():
    """Checking the group size of one"""
    student_identifiers = ['maria', 'dan', 'simon', 'jesse', 'jon', 'michael', 'jacob', 'kapfhammer']
    group_size = len(student_identifiers)/4
    student_groups = parse_gatorgrouper_arguments.check_valid_group_size(group_size,student_identifiers)
    assert student_groups == True

def test_check_valid_group_size_half():
    """Checking the group size of half of the list length"""
    student_identifiers = ['maria', 'dan', 'simon', 'jesse', 'jon', 'michael', 'jacob', 'kapfhammer']
    group_size = len(student_identifiers)/2
    student_groups = parse_gatorgrouper_arguments.check_valid_group_size(group_size,student_identifiers)
    assert student_groups == True

def test_check_valid_group_size_over():
    """Checking the group size of over the list length"""
    student_identifiers = ['maria', 'dan', 'simon', 'jesse', 'jon', 'michael', 'jacob', 'kapfhammer']
    group_size = 9
    student_groups = parse_gatorgrouper_arguments.check_valid_group_size(group_size,student_identifiers)
    assert student_groups == False

def test_display_student_groups(capsys):
    """Checking the display of the student_groups"""
    student_groups = [['gkapfham3', 'gkapfham0'], ['gkapfham1', 'gkapfham4'], ['gkapfham5', 'gkapfham7', 'gkapfham6']]
    group_check = display_student_groups.display_student_groups(student_groups)
    out, err = capsys.readouterr()
    assert out.startswith("('Group', 1)\n")

def test_remove_absent_students_one():
    """Checking to see if absent one student is removed"""
    absent_list = ['Nick']
    list_of_student_of_lists = [['Nick', 0, 1,0], ['Marvin', 0, 1, 1], ["Evin", 1, 1, 0]]
    removed_list = remove_absent_students.remove_absent_students(absent_list, list_of_student_of_lists)
    assert (absent_list in removed_list) is False
    assert len(removed_list) == 2

def test_remove_absent_students_two():
    """Checking to see if absent one student is removed"""
    absent_list = ['Nick', 'Marvin']
    list_of_student_of_lists = [['Nick', 0, 1,0], ['Marvin', 0, 1, 1], ["Evin", 1, 1, 0]]
    removed_list = remove_absent_students.remove_absent_students(absent_list, list_of_student_of_lists)
    assert (absent_list in removed_list) is False
    assert len(removed_list) == 1
