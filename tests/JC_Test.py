
import pytest
import logging
import parse_arguments


from defaults import DEFAULT_CSVFILE
from defaults import DEFAULT_GRPSIZE
from read_student_file import read_student_file


##FileNotFoundError: [Errno 2] No such file or directory: 'students.csv'##

# def test_parse_gatorgrouper_arguments1():
#     args = []
#     parsed_args = parse_arguments.parse_arguments(args)
#     assert parsed_args.logging_level == logging.ERROR
#     assert parsed_args.group_size == defaults.DEFAULT_TEAM_SIZE
#     assert parsed_args.students_file == defaults.DEFAULT_STUDENT_FILE
#     assert parsed_args.grouping_method == grouping_method.RANDOM
#     assert parsed_args.absentees == No

# def test_parse_gatorgrouper_arguments2():
#     f = open('students.csv')
#     args = ['--debug', '--students-file', 'students.csv', '--random']
#     parsed_args = parse_arguments.parse_arguments(args)
#     assert parsed_args.logging_level == logging.DEBUG
#     assert parsed_args.students_file == f


#This one is good
# def test_parse_gatorgrouper_arguments3():
#     args = ['--verbose']
#     parsed_args = parse_arguments.parse_arguments(args)
#     assert parsed_args.logging_level == logging.INFO


def test_parse_gatorgrouper_arguments4():
    args = ['--absentees', 'maria', '--round-robin', '--group-size', '3']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.group_size == 3
    assert parsed_args.group_random == group_random.ROUND_ROBIN
    assert parsed_args.absentees == ['maria']
