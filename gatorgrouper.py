""" GatorGrouper randomly assigns a list of students to groups """

import sys
import logging

import parse_arguments
from read_student_file import read_student_file
from remove_absent_students import remove_absent_students
from display import display_welcome_message
from display import display_student_groups
from display import create_escaped_string_from_list
from group_random import shuffle_students
from group_random import group_random
from group_rrobin import group_rrobin


if __name__ == '__main__':

    # parse the arguments and display welcome message
    GG_ARGUMENTS = parse_arguments.parse_arguments(sys.argv[1:])
    display_welcome_message()
    logging.info("Configuration of GatorGrouper:")
    logging.debug(GG_ARGUMENTS)

    # read in the student identifiers from the specified file
    STUDENT_IDENTIFIERS = remove_absent_students(
        GG_ARGUMENTS.absentees,
        read_student_file(GG_ARGUMENTS.students_file))
    logging.info("GatorGrouper will group these students:")
    logging.info("\n" + create_escaped_string_from_list(STUDENT_IDENTIFIERS))

    # shuffle the student identifiers
    SHUFFLED_STUDENT_IDENTIFIERS = shuffle_students(STUDENT_IDENTIFIERS)
    logging.info("GatorGrouper randomly ordered the students:")
    logging.info("\n" + create_escaped_string_from_list(SHUFFLED_STUDENT_IDENTIFIERS))

    # generate the groups and display them
    if GG_ARGUMENTS.grouping_method == "rrobin":
        GROUPED_STUDENT_IDENTIFIERS = group_rrobin(
            SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.group_size)
    else: # default to random method
        GROUPED_STUDENT_IDENTIFIERS = group_random(
            SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.group_size)

    # report grouping results
    COUNT_GROUPS = len(GROUPED_STUDENT_IDENTIFIERS)
    COUNT_STUDENTS = len(SHUFFLED_STUDENT_IDENTIFIERS)
    logging.info("Successfully placed " + str(COUNT_STUDENTS) +
                 " students into " +str(COUNT_GROUPS) + " groups")

    # report generated groups
    display_student_groups(GROUPED_STUDENT_IDENTIFIERS)
