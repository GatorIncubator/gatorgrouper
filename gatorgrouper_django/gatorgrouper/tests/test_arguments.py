import logging
from utils.parse_arguments import parse_arguments
from utils import defaults
from utils import group_random


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


def test_parse_arguments5():
    args = ['--num-group', '3']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.num_group == 3
