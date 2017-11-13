"""Test suites for the gatorgrouper.py module

run with `pytest test_gatorgrouper.py from the gatorgrouper/tests directory`
Requires `pip3 install pytest-flake8` in order to run.
"""

import gatorgrouper
import logging
import defaults
import string
import random
import display
import remove_absent_students
import parse_arguments
import glob
import os
import group_rrobin
import group_random
from flake8.api import legacy as flake8


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
    list_of_students = [["student1", 0, 1, 0], [
        "student2", 1, 0, 1], ["student3", 1, 1, 0]]
    list_of_absent_students = ["student2"]
    desired_output = [["student1", 0, 1, 0], ["student3", 1, 1, 0]]
    actual_output = remove_absent_students.remove_absent_students(
        list_of_absent_students, list_of_students)
    assert len(list_of_students) == 3
    assert (desired_output == actual_output) is True


def test_group_random1():
    """Testing that the group_random() function creates the
        appropriate number of groups with the appropriate number"""
    list = [
        "Austin",
        "Dan",
        "Angie",
        "Cullen",
        "Chase",
        "Vinny",
        "Nick",
        "Jeff",
        "James",
        "Kelly",
        "Nikki",
        "Robert"]
    list2 = ["Dan", "Angie", "Austin", "Izaak", "Nick", "Jeff"]
    group_size = 3
    group_size2 = 2
    actual_output = group_random.group_random(list, group_size)
    actual_output2 = group_random.group_random(list2, group_size2)
    assert len(actual_output) == 4
    assert len(actual_output[0]) == 3
    assert len(actual_output2) == 3
    assert len(actual_output2[0]) == 2


def test_check_valid_group_size_one():
    """Checking the group size of one"""
    group_size = 1
    student_identifiers = [
        'maria',
        'dan',
        'simon',
        'jesse',
        'jon',
        'michael',
        'jacob',
        'kapfhammer']
    student_groups = parse_arguments.check_valid_group_size(
        group_size, student_identifiers)
    assert student_groups is False


def test_check_valid_group_size_quarter():
    """Checking the group size of one"""
    student_identifiers = [
        'maria',
        'dan',
        'simon',
        'jesse',
        'jon',
        'michael',
        'jacob',
        'kapfhammer']
    group_size = len(student_identifiers) / 4
    student_groups = parse_arguments.check_valid_group_size(
        group_size, student_identifiers)
    assert student_groups


def test_check_valid_group_size_half():
    """Checking the group size of half of the list length"""
    student_identifiers = [
        'maria',
        'dan',
        'simon',
        'jesse',
        'jon',
        'michael',
        'jacob',
        'kapfhammer']
    group_size = len(student_identifiers) / 2
    student_groups = parse_arguments.check_valid_group_size(
        group_size, student_identifiers)
    assert student_groups


def test_check_valid_group_size_over():
    """Checking the group size of over the list length"""
    student_identifiers = [
        'maria',
        'dan',
        'simon',
        'jesse',
        'jon',
        'michael',
        'jacob',
        'kapfhammer']
    group_size = 9
    student_groups = parse_arguments.check_valid_group_size(
        group_size, student_identifiers)
    assert student_groups is False


def test_display_student_groups(capsys):
    """Checking the display of the student_groups"""
    student_groups = [['gkapfham3', 'gkapfham0'], [
        'gkapfham1', 'gkapfham4'], ['gkapfham5', 'gkapfham7', 'gkapfham6']]
    group_check = display.display_student_groups(student_groups)
    out, err = capsys.readouterr()
    assert out.startswith("Group 1")


def test_remove_absent_students_one():
    """Checking to see if absent one student is removed"""
    absent_list = ['Nick']
    list_of_student_of_lists = [['Nick', False, True, False], [
        'Marvin', False, True, True], ["Evin", True, True, False]]
    removed_list = remove_absent_students.remove_absent_students(
        absent_list, list_of_student_of_lists)
    assert (absent_list in removed_list) is False
    assert len(removed_list) == 2


def test_remove_absent_students_two():
    """Checking to see if absent two students is removed"""
    absent_list = ['Nick', 'Marvin']
    list_of_student_of_lists = [['Nick', False, True, False], [
        'Marvin', False, True, True], ["Evin", True, True, False]]
    removed_list = remove_absent_students.remove_absent_students(
        absent_list, list_of_student_of_lists)
    assert (absent_list in removed_list) is False
    assert len(removed_list) == 1


def test_remove_absent_students_all():
    """Checking to see if absent all students are removed"""
    absent_list = ['Nick', 'Marvin', 'Evin']
    list_of_student_of_lists = [['Nick', 0, 1, 0],
                                ['Marvin', 0, 1, 1], ["Evin", 1, 1, 0]]
    correct = []
    removed_list = remove_absent_students.remove_absent_students(
        absent_list, list_of_student_of_lists)
    assert (absent_list in removed_list) is False
    assert len(removed_list) == 0
    assert correct == removed_list


def test_group_random_extra():
    """Testing the random type of grouping with a group of extra people not assigned to their own group"""
    responses = [
        [
            'Nick', True, False, True, False], [
            'Marvin', False, False, True, True], [
                'Evin', True, True, True, False], [
                    'Nikki', True, True, False, False], [
                        'Dan', False, True, False, True]]
    grpsize = 2
    returned_groups = group_random.group_random(responses, grpsize)
    assert len(returned_groups) == 2
    assert grpsize == 2


def test_group_random():
    """Testing the random type of grouping with everyone in an assigned group"""
    responses = [
        [
            'Nick', True, False, True, False], [
            'Marvin', False, False, True, True], [
                'Evin', True, True, True, False], [
                    'Nikki', True, True, False, False], [
                        'Dan', False, True, False, True], [
                            'Michael', True, True, False, False]]
    grpsize = 2
    returned_groups = group_random.group_random(responses, grpsize)
    assert len(returned_groups) == 3


def test_parse_arguments1():
    args = []
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.ERROR
    assert parsed_args.group_size == defaults.DEFAULT_GRPSIZE
    assert parsed_args.students_file == defaults.DEFAULT_CSVFILE
    assert (parsed_args.grouping_method == group_random) is False


def test_parse_arguments2():
    args = ['--debug', '--students-file', 'students.csv', '--random']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.DEBUG
    assert parsed_args.students_file == 'students.csv'
    assert parsed_args.grouping_method == 'random'


def test_parse_gatorgrouper_arguments3():
    args = ['--verbose', '--round-robin']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.INFO
    assert parsed_args.grouping_method == 'rrobin'


def test_parse_arguments4():
    args = ['--absentees', 'maria', '--round-robin', '--group-size', '3']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.group_size == 3
    assert parsed_args.grouping_method == 'rrobin'
    assert parsed_args.absentees == ['maria']


def test_shuffle():
    """Checking the shuffle_students method for appropriate ouput"""
    student_identifiers = [
        "Dan",
        "Nikki",
        "Nick",
        "Jeff",
        "Austin",
        "Simon",
        "Jesse",
        "Maria"]
    shuffled_students = gatorgrouper.shuffle_students(student_identifiers)
    for i in range(0, len(shuffled_students)):
        assert (student_identifiers[i] in shuffled_students) is True
    assert (student_identifiers == shuffled_students) is False


def test_round_robin():
    """Testing the round robin function to assure proper output"""
    list = [
        ["Dan", True, True, True],
        ["Jesse", True, True, True],
        ["Austin", True, True, True],
        ["Nick", False, False, False],
        ["Nikki", False, False, False],
        ["Maria", False, False, False],
        ["Jeff", False, False, False],
        ["Simon", False, False, False],
        ["Jon", False, False, False],
        ["Angie", False, False, False],
        ["Izaak", False, False, False],
        ["Jacob", False, False, False]
    ]
    group_size = 3
    actual_output = group_rrobin.group_rrobin(list, group_size)
    assert len(actual_output) == 4
    assert len(actual_output[0]) == group_size
    assert (["Dan", True, True, True] in actual_output[0]) is True
    assert (["Jesse", True, True, True] in actual_output[2]) is True
    assert (["Austin", True, True, True] in actual_output[1]) is True


def test_random():
    """Testing the random grouping function to assure proper output"""
    list = [
        ["Dan", True, True, True],
        ["Jesse", True, True, True],
        ["Austin", True, True, True],
        ["Nick", False, False, False],
        ["Nikki", False, False, False],
        ["Maria", False, False, False],
        ["Jeff", False, False, False],
        ["Simon", False, False, False],
        ["Jon", False, False, False],
        ["Angie", False, False, False],
        ["Izaak", False, False, False],
        ["Jacob", False, False, False]
    ]
    group_size = 4
    actual_output = group_random.group_random(list, group_size)
    assert len(actual_output) == 3
    assert len(actual_output[0]) == 4

def test_group_rrobin_num_group():
    """Testing the round robin group number fucntion to assure proper output"""
    list = [
                ["Dan", True, True, True],
                ["Jesse", True, True, True],
                ["Austin", True, True, True],
                ["Nick", False, False, False],
                ["Nikki", False, False, False],
                ["Maria", False, False, False],
                ["Jeff", False, False, False],
                ["Simon", False, False, False],
                ["Jon", False, False, False],
                ["Angie", False, False, False],
                ["Izaak", False, False, False],
                ["Jacob", False, False, False]
    ]
    group_size = 3
    actual_output = group_rrobin_num_group.group_rrobin_num_group(list, group_size)
    assert len(actual_output) == 4
    assert len(actual_output[0]) == group_size
    assert (["Dan", True, True, True] in actual_output[0]) is True
    assert (["Jesse", True, True, True] in actual_output[2]) is True
    assert (["Austin", True, True, True] in actual_output[1]) is True
# Linting Tests
def test_flake8():

    # list of all file names to be checked for PEP8
    filenames = list()

    # fill list with all python files found in all subdirectories
    for root, dirs, files in os.walk("gatorgrouper", topdown=False):
        pyFiles = glob.glob(root + "/*.py")
        filenames.extend(pyFiles)

    style_guide = flake8.get_style_guide(ignore=["E265", "E501"])
    report = style_guide.check_files(filenames)
    assert report.get_statistics('E') == [], 'Flake8 found violations'
