""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys

DEFALT_STUDENT_FILE = "students.txt"
DEFAULT_TEAM_SIZE = 2
GATORGROUPER_HOME = "GATORGROUPER_HOME"


def parse_gatorgrader_arguments(args):
    """ Parses the arguments provided on the command-line """
    gg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    gg_parser.add_argument(
        "--verbose",
        help="Display verbose diagnostic information",
        action="store_true")

    gg_parser.add_argument(
        "--group-size",
        help="Number of students in a group",
        type=int,
        default=DEFAULT_TEAM_SIZE,
        required=False)

    gg_parser.add_argument(
        "--students-file",
        help="File containing last name of students",
        type=str,
        default=DEFALT_STUDENT_FILE,
        required=False)

    gg_arguments_finished = gg_parser.parse_args(args)
    return gg_arguments_finished


def read_student_file(students_file_name):
    """ Reads the student identifies from the specific file,
        returning the identifiers in a list"""
    with open(students_file_name, 'r') as students_file:
        student_identifers = [line.strip() for line in students_file]
    return student_identifers


def display_student_identifiers(student_identifers):
    """ Display the student identifiers """
    for student in student_identifers:
        print(student)


def shuffle_students(student_identifers):
    """ Shuffle the student identifiers """
    shuffled_student_identifers = student_identifers[:]
    shuffle(shuffled_student_identifers)
    return shuffled_student_identifers


def group_students_itertools(student_identifers, group_size):
    """ Group the student identifiers """
    iterable = iter(student_identifers)
    return list(iter(lambda: list(itertools.islice(iterable, group_size)), []))


def display_welcome_message():
    """ Display a welcome message """
    print()
    print("GatorGrouper: Automatically Assign Students to Groups")
    print("https://github.com/gkapfham/gatorgrouper")
    print()


if __name__ == '__main__':
    # parse the arguments and display welcome message
    gg_arguments = parse_gatorgrader_arguments(sys.argv[1:])
    display_welcome_message()
    if gg_arguments.verbose is True:
        print("Configuration of GatorGrouper:")
        print(gg_arguments)
        print()
    # read in the student identifiers from the specified file
    student_identifers = read_student_file(gg_arguments.students_file)
    if gg_arguments.verbose is True:
        print("GatorGrouper will group these students:")
        print()
        display_student_identifiers(student_identifers)
        print()
    # shuffle the student identifiers
    shuffled_student_identifers = shuffle_students(student_identifers)
    if gg_arguments.verbose is True:
        print("GatorGrouper randomly ordered the students:")
        print()
        display_student_identifiers(shuffled_student_identifers)
        print()
    # generate the groups and display them
    grouped_student_identifiers = group_students_itertools(shuffled_student_identifers,
                                                 gg_arguments.group_size)
    print(grouped_student_identifiers)
