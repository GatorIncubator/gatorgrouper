from src.controllers import display


def test_display_student_groups(capsys):
    """Checking the display of the student_groups"""
    student_groups = [['gkapfham3', 'gkapfham0'], [
        'gkapfham1', 'gkapfham4'], ['gkapfham5', 'gkapfham7', 'gkapfham6']]
    display.display_student_groups(student_groups)
    out, err = capsys.readouterr()
    assert out.startswith('\033[0;32m' + '\033[1m' + '\033[4m' + "Group 1")


def test_display_welcome_message():
    """ Test if the welcome message is correctly displayed"""
    expected_output = "\nGatorGrouper: Automatically Assign Students to Groups\nhttps://github.com/GatorGrouper/gatorgrouper\n"
    output = display.display_welcome_message()
    assert output == expected_output
