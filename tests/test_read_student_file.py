import read_student_file

def test_read_file_populates_csvdata_0():
    """Checks that the read student file populates data from a CSV."""
    # assert len(read_student_file.read_student_file("tests/students.csv")) == 28
    # read_student_file.read_file("tests/students.csv")
    assert len(read_student_file.read_student_file("tests/students.csv")) != 0
