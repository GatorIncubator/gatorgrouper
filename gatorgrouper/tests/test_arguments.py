"""Command line argument testing"""
import logging
from utils import parse_arguments
from utils import group_creation
from utils import constants


def test_parse_arguments1():
    """General testing of arguments - if arguments exists"""
    args = []
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.ERROR
    assert parsed_args.group_size == constants.DEFAULT_GRPSIZE
    assert parsed_args.students_file == constants.DEFAULT_CSVFILE
    assert parsed_args.method != constants.DEFAULT_METHOD


def test_parse_arguments2():
    """Testing specfied arguments"""
    args = ["--debug", "--students-file", "students.csv", "--random"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.DEBUG
    assert parsed_args.students_file == "students.csv"
    assert parsed_args.method == "random"


def test_parse_gatorgrouper_arguments3():
    """Testing specfied arguments"""
    args = ["--verbose", "--round-robin"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.INFO
    assert parsed_args.method == constants.ALGORITHM_ROUND_ROBIN


def test_parse_arguments4():
    """Testing specfied arguments"""
    args = ["--absentees", "maria", "--round-robin", "--group-size", "3"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.group_size == 3
    assert parsed_args.method == constants.ALGORITHM_ROUND_ROBIN
    assert parsed_args.absentees == ["maria"]


def test_parse_arguments5():
    """Testing specfied arguments"""
    args = ["--num-group", "3"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.num_group == 3
