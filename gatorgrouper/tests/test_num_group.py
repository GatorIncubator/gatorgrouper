"""Testing number of groups"""
from utils import parse_arguments


def test_check_number_groups_size_zero():
    """Checking 0 groups"""
    numgrp = 0
    student_identifiers = [
        "maria",
        "dan",
        "simon",
        "jesse",
        "jon",
        "michael",
        "jacob",
        "kapfhammer",
    ]
    student_groups = parse_arguments.check_valid_num_group(numgrp, student_identifiers)
    assert student_groups


def test_check_number_groups_size_one():
    """Checking 1 group"""
    numgrp = 1
    student_identifiers = [
        "maria",
        "dan",
        "simon",
        "jesse",
        "jon",
        "michael",
        "jacob",
        "kapfhammer",
    ]
    student_groups = parse_arguments.check_valid_num_group(numgrp, student_identifiers)
    assert student_groups


def test_check_number_groups_size_multi():
    """Checking multiple group"""
    numgrp = 2
    numgrp2 = 3
    student_identifiers = [
        "maria",
        "dan",
        "simon",
        "jesse",
        "jon",
        "michael",
        "jacob",
        "kapfhammer",
    ]
    student_groups = parse_arguments.check_valid_num_group(numgrp, student_identifiers)
    student_groups2 = parse_arguments.check_valid_num_group(
        numgrp2, student_identifiers
    )
    assert student_groups
    assert student_groups2


def test_check_number_groups_over():
    """Checking if the number of groups greater than number of students"""
    numgrp = 9
    student_identifiers = [
        "maria",
        "dan",
        "simon",
        "jesse",
        "jon",
        "michael",
        "jacob",
        "kapfhammer",
    ]
    student_groups = parse_arguments.check_valid_num_group(numgrp, student_identifiers)
    assert student_groups is False
