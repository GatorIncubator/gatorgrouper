"""Testing if absent.py correctly handles being absent"""
from utils import remove_absent_students


def test_remove_missing_students():
    """Testing the remove_missing_students() function with
        an input that includes one absent student"""
    list_of_students = [
        ["student1", 0, 1, 0],
        ["student2", 1, 0, 1],
        ["student3", 1, 1, 0],
    ]
    list_of_absent_students = ["student2"]
    desired_output = [["student1", 0, 1, 0], ["student3", 1, 1, 0]]
    actual_output = remove_absent_students.remove_missing_students(
        list_of_absent_students, list_of_students
    )
    assert len(list_of_students) == 3
    assert (desired_output == actual_output) is True


def test_remove_missing_students_one():
    """Checking to see if absent one student is removed"""
    absent_list = ["Nick"]
    list_of_student_of_lists = [
        ["Nick", False, True, False],
        ["Marvin", False, True, True],
        ["Evin", True, True, False],
    ]
    removed_list = remove_absent_students.remove_missing_students(
        absent_list, list_of_student_of_lists
    )
    assert (absent_list in removed_list) is False
    assert len(removed_list) == 2


def test_remove_missing_students_two():
    """Checking to see if absent two students is removed"""
    absent_list = ["Nick", "Marvin"]
    list_of_student_of_lists = [
        ["Nick", False, True, False],
        ["Marvin", False, True, True],
        ["Evin", True, True, False],
    ]
    removed_list = remove_absent_students.remove_missing_students(
        absent_list, list_of_student_of_lists
    )
    assert (absent_list in removed_list) is False
    assert len(removed_list) == 1


def test_remove_missing_students_all():
    """Checking to see if absent all students are removed"""
    absent_list = ["Nick", "Marvin", "Evin"]
    list_of_student_of_lists = [
        ["Nick", 0, 1, 0],
        ["Marvin", 0, 1, 1],
        ["Evin", 1, 1, 0],
    ]
    correct = []
    removed_list = remove_absent_students.remove_missing_students(
        absent_list, list_of_student_of_lists
    )
    assert (absent_list in removed_list) is False
    # is the list empty
    assert not removed_list
    assert correct == removed_list
