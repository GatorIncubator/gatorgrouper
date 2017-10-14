""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys

DEFALT_STUDENT_FILE = "students.txt"
GATORGROUPER_HOME = "GATORGROUPER_HOME"

DEFAULT_TEAM_SIZE = 2
SINGLETON_GROUP = 1


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
    """ Reads the student identifiers from the specific file,
        returning the identifiers in a list """
    with open(students_file_name, 'r') as students_file:
        student_identifiers = [line.strip() for line in students_file]
    return student_identifiers


def display_diagnostics(student_identifiers, student_groups):
    """ Display information about what was generated """
    print("Successfully placed",
          len(student_identifiers), "students into",
          len(student_groups), "groups")
    print()


def display_student_identifiers(student_identifiers):
    """ Display the student identifiers """
    for student in student_identifiers:
        print(student)


def display_student_groups(student_groups):
    """ Display the student groups with labels """
    group_counter = 1
    for student_group in student_groups:
        print("Group", group_counter)
        print(*student_group)
        print()
        group_counter = group_counter + 1


def shuffle_students(student_identifiers):
    """ Shuffle the student identifiers """
    shuffled_student_identifiers = student_identifiers[:]
    shuffle(shuffled_student_identifiers)
    return shuffled_student_identifiers


def group_students(student_identifiers, group_size):
    """ Group the student identifiers """
    iterable = iter(student_identifiers)
    # use itertools to chunk the students into groups
    student_groups = list(
        iter(lambda: list(itertools.islice(iterable, group_size)), []))
    # merge a single student into the previous group
    last_group_index = len(student_groups) - 1
    if len(student_groups[last_group_index]) == SINGLETON_GROUP:
        receiving_group = student_groups[last_group_index - 1]
        too_small_group = student_groups[last_group_index]
        receiving_group.append(*too_small_group)
        student_groups.remove(too_small_group)
    return student_groups


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
    student_identifiers = read_student_file(gg_arguments.students_file)
    if gg_arguments.verbose is True:
        print("GatorGrouper will group these students:")
        print()
        display_student_identifiers(student_identifiers)
        print()
    # shuffle the student identifiers
    shuffled_student_identifiers = shuffle_students(student_identifiers)
    if gg_arguments.verbose is True:
        print("GatorGrouper randomly ordered the students:")
        print()
        display_student_identifiers(shuffled_student_identifiers)
        print()
    # generate the groups and display them
    grouped_student_identifiers = group_students(shuffled_student_identifiers,
                                                 gg_arguments.group_size)
    display_diagnostics(shuffled_student_identifiers,
                        grouped_student_identifiers)
    display_student_groups(grouped_student_identifiers)
