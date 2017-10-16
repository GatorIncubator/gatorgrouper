
import pytest
import logging
import grouping_method
import defaults
import gatorgrouper

def test_parse_gatorgrouper_arguments1(args):
    args = []
    parsed_args = parse_gatorgrouper_arguments(args)
    assert parsed_args.logging_level == logging.ERROR
    assert parsed_args.group_size == defaults.DEFAULT_TEAM_SIZE
    assert parsed_args.students_file == defaults.DEFAULT_STUDENT_FILE
    assert parsed_args.grouping_method == grouping_method.RANDOM
    assert parsed_args.absentees == No

def test_parse_gatorgrouper_arguments2(args):
    args = ['--debug', '--students-file', 'students.csv', '--random']
    parsed_args = parse_gatorgrouper_arguments(args)
    assert parsed_args.logging_level == logging.DEBUG
    assert parsed_args.students_file == 'students.csv'
    assert parsed_args.grouping_method == grouping_method.RANDOM

def test_parse_gatorgrouper_arguments3(args):
    args = ['--verbose', '--sudoku']
    parsed_args = parse_gatorgrouper_arguments(args)
    assert parsed_args.logging_level == logging.INFO
    assert parsed_args.grouping_method == grouping_method.SUDOKU

def test_parse_gatorgrouper_arguments4(args):
    args = ['--absentees', 'maria', '--round-robin', '--group-size', '3']
    parsed_args = parse_gatorgrouper_arguments(args)
    assert parsed_args.group_size == 3
    assert parsed_args.grouping_method == grouping_method.ROUND_ROBIN
    assert parsed_args.absentees == ['maria']

# def test_display_diagnostics(student_identifers, student_groups):
#     student_identifers = len(student_identifers)
#     student_groups = len(student_groups)
#     assert  student_identifers == len(student_identifers)
#     assert  student_groups == len(student_groups)
