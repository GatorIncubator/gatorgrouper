"""Testing group size"""
import parse_arguments


def test_check_valid_group_size_one():
    """Checking the group size of one"""
    group_size = 1
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
    student_groups = parse_arguments.check_valid_group_size(
        group_size, student_identifiers
    )
    assert student_groups is False


def test_check_valid_group_size_quarter():
    """Checking the group size of one"""
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
    group_size = len(student_identifiers) // 4
    student_groups = parse_arguments.check_valid_group_size(
        group_size, student_identifiers
    )
    assert student_groups


def test_check_valid_group_size_half():
    """Checking the group size of half of the list length"""
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
    group_size = len(student_identifiers) // 2
    student_groups = parse_arguments.check_valid_group_size(
        group_size, student_identifiers
    )
    assert student_groups


def test_check_valid_group_size_over():
    """Checking the group size of over the list length"""
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
    group_size = 9
    student_groups = parse_arguments.check_valid_group_size(
        group_size, student_identifiers
    )
    assert student_groups is False
