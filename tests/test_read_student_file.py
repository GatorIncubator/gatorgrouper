""" Testing read_student_file """

from gatorgrouper.utils import read_student_file


def test_read_student_file(generate_csv):
    """ Test read_student_file """
    expectedoutput = [["delgrecoj", True, True, False, True]]
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
