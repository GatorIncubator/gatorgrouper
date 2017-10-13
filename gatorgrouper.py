""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys
#function files
from parse_gatorgrader_arguments import parse_gatorgrader_arguments
from read_student_file import read_student_file
from display_diagnostics import display_diagnostics
from display_student_identifiers import display_student_identifiers
from display_student_groups import display_student_groups
from shuffle_students import shuffle_students
from group_students import *
from display_welcome_message import display_welcome_message
from group_students_categories import group_students_categories


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
    grouped_student_identifiers = group_students_categories(shuffled_student_identifers,
                                                 gg_arguments.group_size)
    display_diagnostics(shuffled_student_identifers,
                        grouped_student_identifiers)
    display_student_groups(grouped_student_identifiers)
    
