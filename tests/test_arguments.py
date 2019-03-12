"""Command line argument testing"""

import logging
import pytest
from gatorgrouper.utils import parse_arguments
from gatorgrouper.utils import constants
from gatorgrouper.utils import read_student_file


def test_parse_arguments1(no_arguments, capsys):
    """No command-line arguments is incorrect"""
    with pytest.raises(SystemExit):
        parse_arguments.parse_arguments(no_arguments)
    standard_out, standard_err = capsys.readouterr()
    assert standard_out is constants.EMPTY_STRING
    assert constants.ERROR in standard_err


def test_parse_arguments2(generate_csv):
    """Testing specfied arguments"""
    args = ["--debug", "--file", generate_csv, "--method=random"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.DEBUG
    assert "csvNg.csv" in parsed_args.file
    assert parsed_args.method == constants.ALGORITHM_RANDOM


def test_parse_gatorgrouper_arguments3(generate_csv):
    """Testing specfied arguments"""
    args = ["--verbose", "--file", generate_csv, "--method=rrobin"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.INFO
    assert parsed_args.method == constants.ALGORITHM_ROUND_ROBIN


def test_parse_arguments4(generate_csv):
    """Testing specfied arguments"""
    args = [
        "--absentees",
        "maria",
        "--file",
        generate_csv,
        "--method=rrobin",
        "--group-size",
        "3",
    ]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.group_size == 3
    assert parsed_args.method == constants.ALGORITHM_ROUND_ROBIN
    assert parsed_args.absentees == ["maria"]


def test_parse_arguments5(generate_csv):
    """Testing specfied arguments"""
    args = ["--file", generate_csv, "--num-group", "3"]
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.num_group == 3


def test_file_argument_verifiable(generate_csv):
    """Check that valid file arguments will verify correctly"""
    correct_arguments = ["--file", generate_csv]
    parsed_arguments = parse_arguments.parse_arguments(correct_arguments)
    input_list = read_student_file.read_csv_data(parsed_arguments.file)
    checker = parse_arguments.check_valid(parsed_arguments, input_list)
    assert checker is True


def test_file_argument_invalid():
    """Check that invalid file arguments will not verify correctly"""
    wrong_arguments = ["--file", "x"]
    parsed_arguments = parse_arguments.parse_arguments(wrong_arguments)
    input_list = read_student_file.read_csv_data(parsed_arguments.file)
    checker = parse_arguments.check_valid(parsed_arguments, input_list)
    assert checker is False


def test_file_argument_empty():
    """Check that invalid file arguments will not verify correctly"""
    wrong_arguments = ["--file", ""]
    parsed_arguments = parse_arguments.parse_arguments(wrong_arguments)
    input_list = read_student_file.read_csv_data(parsed_arguments.file)
    checker = parse_arguments.check_valid(parsed_arguments, input_list)
    assert checker is False


def test_valid_size(generate_csv):
    """Check that valid size arguments will not verify correctly"""
    correct_arguments = ["--file", generate_csv, "--group-size", "3"]
    parsed_arguments = parse_arguments.parse_arguments(correct_arguments)
    input_list = read_student_file.read_csv_data(parsed_arguments.file)
    checker = parse_arguments.check_valid(parsed_arguments, input_list)
    assert checker is True


def test_invalid_input(generate_csv):
    """Check that invalid size and number arguments will not verify correctly"""
    wrong_arguments = ["--file", generate_csv, "--group-size", "7", "--num-group", "7"]
    parsed_arguments = parse_arguments.parse_arguments(wrong_arguments)
    input_list = read_student_file.read_csv_data(parsed_arguments.file)
    checker = parse_arguments.check_valid(parsed_arguments, input_list)
    assert checker is False
