"""Testing the display  """

from utils import display


def test_display_student_groups(capsys):
    """Checking the display of the student_groups"""
    student_groups = [
        ["gkapfham3", "gkapfham0"],
        ["gkapfham1", "gkapfham4"],
        ["gkapfham5", "gkapfham7", "gkapfham6"],
    ]
    display.display_student_groups(student_groups)
    out, _ = capsys.readouterr()
    assert out.startswith("\033[0;32m" + "\033[1m" + "\033[4m" + "Group 1")


def test_display_welcome_message(capsys):
    """ Test if the welcome message is correctly displayed"""
    display.display_welcome_message()
    captured = capsys.readouterr()
    expected_output = """
GatorGrouper: Automatically Assign Students to Groups
https://github.com/GatorEducator/gatorgrouper

"""
    assert captured.out == expected_output
