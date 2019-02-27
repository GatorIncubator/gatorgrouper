"""Testing number of groups"""
from utils import read_student_file


def test_read_file_populates_csvdata_0():
    """Checks that the read student file populates data from a CSV."""
    assert len(read_student_file.read_student_file("gatorgrouper/tests/students.csv")) != 0
