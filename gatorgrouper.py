""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys
import logging

import parse_gatorgrouper_arguments
from read_student_file import read_student_file
from create_escaped_string_from_list import create_escaped_string_from_list
from display_student_groups import display_student_groups
from shuffle_students import shuffle_students
from group_students import *
from display_welcome_message import display_welcome_message


if __name__ == '__main__':
    # parse the arguments and display welcome message
    gg_arguments = parse_gatorgrouper_arguments.parse_gatorgrouper_arguments(sys.argv[1:])
    display_welcome_message()
    logging.info("Configuration of GatorGrouper:")
    logging.debug(gg_arguments)

    # read in the student identifiers from the specified file
    student_identifiers = read_student_file(gg_arguments.students_file)
    logging.info("GatorGrouper will group these students:")
    logging.info("\n" + create_escaped_string_from_list(student_identifiers))

    # shuffle the student identifiers
    shuffled_student_identifiers = shuffle_students(student_identifiers)
    logging.info("GatorGrouper randomly ordered the students:")
    logging.info("\n" + create_escaped_string_from_list(shuffled_student_identifiers))

    # generate the groups and display them
    grouped_student_identifiers = group_students(shuffled_student_identifiers,
                                                 gg_arguments.group_size)

    logging.info("Successfully placed " + str(len(shuffled_student_identifiers)) + " students into " + str(len(grouped_student_identifiers)) + " groups")

    display_student_groups(grouped_student_identifiers)
