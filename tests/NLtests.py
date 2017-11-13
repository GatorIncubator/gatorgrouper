import pytest
import random

def test_shuffle (student_identifiers):
    """Checking to see if any students were lost"""
    student_identifiers = ['gkapfham3', 'gkapfham0', 'gkapfham1', 'gkapfham4', 'gkapfham5', 'gkapfham7', 'gkapfham6']
    shuffled_students = shuffle_students(student_identifiers)
    if shuffled_students contains student_identifiers
        assert student_identifiers == True
