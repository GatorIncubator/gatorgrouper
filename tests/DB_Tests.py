"""Test suites for the gatorgrouper.py module"""

import pytest
import itertools
import gatorgrouper
import logging
import grouping_method
import defaults
import string
import random
import parse_gatorgrouper_arguments
import display_student_groups
import sys
import remove_absent_students

def test_create_escaped_string_from_list():
    """Testing the create_escaped_string_from_list() function 
        with a list of normal input size"""
    list = ["Dan", "Nick", "Jeff", "Nikki", "Angie", "Austin"]
    desired_output_string = "Dan\nNick\nJeff\nNikki\nAngie\nAustin\n"
    actual_output_string = gatorgrouper.create_escaped_string_from_list(list)
    assert len(list) == 6
    assert ("Dan" in actual_output_string) is True
    assert ("Austin" in actual_output_string) is True
    assert (desired_output_string == actual_output_string) is True


def test_create_escaped_string_from_list_with_empty_list():
    """Testing the create_escaped_string_from_list() function
        with an empty list as input"""
    list = []
    desired_output_string = ""
    actual_output_string = gatorgrouper.create_escaped_string_from_list(list)
    assert len(list) == 0
    assert (desired_output_string == actual_output_string) is True


def test_create_escaped_string_from_list_with_large_list():
    """Testing the create_escaped_string_from_list() function 
        with a list of large input size"""
    list = []
    extra_list = []
    desired_output_string = ""
    chars = string.ascii_uppercase + string.ascii_lowercase

    # populate the list with 250 random strings 
    for i in range(0, 250):
        random_string = ''.join(random.choice(chars) for _ in range(5))
        list.append(random_string)
        extra_list.append(random_string + '\n')

    # add the new line character at the end of each string in the list
    desired_output_string = ''.join(extra_list)
    # running the function with our large input list 
    actual_output_string = gatorgrouper.create_escaped_string_from_list(list)

    assert len(list) == 250
    assert len(extra_list) == 250
    assert (desired_output_string == actual_output_string) is True


def test_remove_absent_students():
    """Testing the remove_absent_students() function with
        an input that includes one absent student"""
    list_of_students = [["student1",0,1,0], ["student2",1,0,1], ["student3",1,1,0]]
    list_of_absent_students = ["student2"]
    desired_output = [["student1",0,1,0], ["student3",1,1,0]]
    actual_output = remove_absent_students.remove_absent_students(list_of_absent_students, list_of_students)
    assert len(list_of_students) == 3
    assert (desired_output == actual_output) is True 


#def test_group_random():
    """Testing that the group_random() function behaves
        appropriately"""





