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
from group_random import group_random_group_size
from group_random import group_random_num_group
from group_rrobin import group_rrobin_group_size
from group_rrobin import group_rrobin_num_group
from spreadsheet import create_csv
from defaults import DEFAULT_CSVFILE
from defaults import DEFAULT_NUMGRP


if __name__ == "__main__":

    # parse the arguments and display welcome message
    GG_ARGUMENTS = parse_arguments.parse_arguments(sys.argv[1:])
    display_welcome_message()
    logging.info("Configuration of GatorGrouper:")
    logging.debug(GG_ARGUMENTS)

    # skip pulling from Google Sheets if CSV is provided
    if GG_ARGUMENTS.students_file == DEFAULT_CSVFILE:
        logging.info("Pulling CSV file from Google Sheets.")
        create_csv()
    else:
        logging.info("Using the CSV file provided")

    # read in the student identifiers from the specified file
    print(GG_ARGUMENTS.students_file)
    STUDENT_IDENTIFIERS = remove_absent_students(
        GG_ARGUMENTS.absentees, read_student_file(GG_ARGUMENTS.students_file)
    )
    logging.info("GatorGrouper will group these students:")
    logging.info("\n %s", create_escaped_string_from_list(STUDENT_IDENTIFIERS))

    # shuffle the student identifiers
    SHUFFLED_STUDENT_IDENTIFIERS = shuffle_students(STUDENT_IDENTIFIERS)
    logging.info("GatorGrouper randomly ordered the students:")
    logging.info("\n %s", create_escaped_string_from_list(SHUFFLED_STUDENT_IDENTIFIERS))

    # generate the groups and display them
    # pylint: disable=bad-continuation
    if (
        GG_ARGUMENTS.grouping_method == "rrobin"
        and GG_ARGUMENTS.num_group is DEFAULT_NUMGRP
    ):
        GROUPED_STUDENT_IDENTIFIERS = group_rrobin_group_size(
            SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.group_size
        )
    elif (
        GG_ARGUMENTS.grouping_method == "rrobin"
        and GG_ARGUMENTS.num_group is not DEFAULT_NUMGRP
    ):
        GROUPED_STUDENT_IDENTIFIERS = group_rrobin_num_group(
            SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.num_group
        )
    elif GG_ARGUMENTS.num_group is DEFAULT_NUMGRP:  # default to random method
        GROUPED_STUDENT_IDENTIFIERS = group_random_group_size(
            SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.group_size
        )
    else:
        GROUPED_STUDENT_IDENTIFIERS = group_random_num_group(
            SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.num_group
        )

    # report grouping results
    COUNT_GROUPS = len(GROUPED_STUDENT_IDENTIFIERS)
    COUNT_STUDENTS = len(SHUFFLED_STUDENT_IDENTIFIERS)
    logging.info(
        "Successfully placed %d students into %d groups ", COUNT_STUDENTS, COUNT_GROUPS
    )

    # report generated groups
    display_student_groups(GROUPED_STUDENT_IDENTIFIERS)
