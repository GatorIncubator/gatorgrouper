"""Command line argument testing"""
import logging
from utils import parse_arguments
from utils import constants
from utils import group_random
from utils import constants


def test_parse_arguments2(generate_csv):
    """Testing specfied arguments"""
    args = ["--debug", "--file", generate_csv, "--random"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.DEBUG
    assert "csvNg.csv" in parsed_args.file
    assert parsed_args.grouping_method == constants.ALGORITHM_RANDOM


def test_parse_gatorgrouper_arguments3(generate_csv):
    """Testing specfied arguments"""
    args = ["--verbose", "--file", generate_csv, "--rrobin"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.INFO
    assert parsed_args.grouping_method == constants.ALGORITHM_ROUND_ROBIN


def test_parse_arguments4(generate_csv):
    """Testing specfied arguments"""
    args = ["--absentees", "maria", "--file", generate_csv, "--rrobin", "--group-size", "3"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.group_size == 3
    assert parsed_args.grouping_method == constants.ALGORITHM_ROUND_ROBIN
    assert parsed_args.absentees == ["maria"]


def test_parse_arguments5(generate_csv):
    """Testing specfied arguments"""
    args = ["--file", generate_csv, "--num-group", "3"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.num_group == 3
