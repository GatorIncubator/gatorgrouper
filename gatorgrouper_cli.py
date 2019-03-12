""" GatorGrouper randomly assigns a list of students to groups """

import sys
import logging

from gatorgrouper.utils import parse_arguments
from gatorgrouper.utils import remove_absent_students
from gatorgrouper.utils import read_student_file
from gatorgrouper.utils import group_creation
from gatorgrouper.utils import group_graph
from gatorgrouper.utils import display
from gatorgrouper.utils import constants


if __name__ == "__main__":  # pragma: no cover

    # parse the arguments and display welcome message
    GG_ARGUMENTS = parse_arguments.parse_arguments(sys.argv[1:])
    display.display_welcome_message()
    logging.info("Configuration of GatorGrouper:")
    logging.debug(GG_ARGUMENTS)

    # read in the student identifiers from the specified file
    input_list = read_student_file.read_csv_data(GG_ARGUMENTS.file)
    check_if_arguments_valid = parse_arguments.check_valid(GG_ARGUMENTS, input_list)
    if check_if_arguments_valid is False:
        print("Incorrect command-line arguments.")
        sys.exit(1)
    else:
        STUDENT_IDENTIFIERS = remove_absent_students.remove_missing_students(
            GG_ARGUMENTS.absentees, read_student_file.read_csv_data(GG_ARGUMENTS.file)
        )
        logging.info("GatorGrouper will group these students:")
        logging.info(
            "\n %s", display.create_escaped_string_from_list(STUDENT_IDENTIFIERS)
        )

        # shuffle the student identifiers
        SHUFFLED_STUDENT_IDENTIFIERS = group_creation.shuffle_students(
            STUDENT_IDENTIFIERS
        )
        logging.info("GatorGrouper randomly ordered the students:")
        logging.info(
            "\n %s",
            display.create_escaped_string_from_list(SHUFFLED_STUDENT_IDENTIFIERS),
        )

        # generate the groups and display them
        # pylint: disable=bad-continuation
        if (
            GG_ARGUMENTS.method == constants.ALGORITHM_ROUND_ROBIN
            and GG_ARGUMENTS.num_group is constants.DEFAULT_NUMGRP
        ):
            GROUPED_STUDENT_IDENTIFIERS = group_creation.group_rrobin_group_size(
                SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.group_size
            )
        elif (
            GG_ARGUMENTS.method == constants.ALGORITHM_ROUND_ROBIN
            and GG_ARGUMENTS.num_group is not constants.DEFAULT_NUMGRP
        ):
            GROUPED_STUDENT_IDENTIFIERS = group_creation.group_rrobin_num_group(
                SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.num_group
            )
        elif (
            GG_ARGUMENTS.method == constants.ALGORITHM_GRAPH
            and GG_ARGUMENTS.num_group is not constants.DEFAULT_NUMGRP
        ):
            GROUPED_STUDENT_IDENTIFIERS = group_graph.group_graph_partition(
                SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.num_group
            )
        elif (
            GG_ARGUMENTS.num_group is constants.DEFAULT_NUMGRP
        ):  # default to random method
            GROUPED_STUDENT_IDENTIFIERS = group_creation.group_random_group_size(
                SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.group_size
            )
        else:
            GROUPED_STUDENT_IDENTIFIERS = group_creation.group_random_num_group(
                SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.num_group
            )
        # report grouping results
        COUNT_GROUPS = len(GROUPED_STUDENT_IDENTIFIERS)
        COUNT_STUDENTS = len(SHUFFLED_STUDENT_IDENTIFIERS)
        logging.info(
            "Successfully placed %d students into %d groups ",
            COUNT_STUDENTS,
            COUNT_GROUPS,
        )

        # report generated groups
        display.display_student_groups(GROUPED_STUDENT_IDENTIFIERS)
