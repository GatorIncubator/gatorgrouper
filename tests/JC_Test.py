
import pytest
import logging
import parse_arguments
import group_random
import defaults




def test_parse_gatorgrouper_arguments1():
    args = []
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.ERROR
    assert parsed_args.group_size == defaults.DEFAULT_GRPSIZE
    assert parsed_args.students_file == defaults.DEFAULT_CSVFILE
    assert parsed_args.absentees == None

def test_parse_gatorgrouper_arguments2():
    # Need to set a path so ther assetion for student file is checking in the
    #gatorgrouper directory. Temp fix is to have the student.csv file in the
    #test folder
    args = ['--debug', '--students-file', 'students.csv', '--random']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.DEBUG
    assert parsed_args.students_file == 'students.csv'

def test_parse_gatorgrouper_arguments3():
    args = ['--verbose']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.INFO


def test_parse_gatorgrouper_arguments4():
    args = ['--absentees', 'maria', '--group-size', '3']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.group_size == 3
    assert parsed_args.absentees == ['maria']
