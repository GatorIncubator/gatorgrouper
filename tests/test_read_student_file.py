""" Testing read_student_file """

from gatorgrouper.utils import read_student_file


def test_read_student_file(generate_csv):
    """ Test read_student_file """
    expectedoutput = [
        ["delgrecoj", True, True, False, True],
        ["delgrecoj2", True, True, False, True],
        ["delgrecoj3", True, True, False, True],
        ["delgrecoj4", True, True, False, True],
        ["delgrecoj5", True, True, False, True],
        ["delgrecoj6", True, True, False, True],
    ]
    assert read_student_file.read_csv_data(generate_csv) == expectedoutput


def test_no_file_found():
    """ No file found """
    assert read_student_file.read_csv_data("fakepath") == ""


def test_read_student_file_no_header(generate_csv_no_header):
    """ Test read_student_file """
    expectedoutput = [
        ["delgrecoj", True, True, False, True],
        ["delgrecoj2", True, True, True, True],
    ]
    assert read_student_file.read_csv_data(generate_csv_no_header) == expectedoutput


def test_read_student_file_float(generate_csv_float):
    """ Test read_student_file """
    expectedoutput = [["delgrecoj", 1.2, 1.1, 0.9, 2.3]]
    assert read_student_file.read_csv_data(generate_csv_float) == expectedoutput


def test_read_student_file_no_header_float(generate_csv_float_no_header):
    """ Test read_student_file """
    expectedoutput = [
        ["delgrecoj", 1.2, 0.7, 1.1, 0.2],
        ["delgrecoj2", 0.1, 0.5, 0.8, 0.6],
    ]
    assert (
        read_student_file.read_csv_data(generate_csv_float_no_header) == expectedoutput
    )
