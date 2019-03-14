""" Run all arguments which were passed in to main program """

import logging

from gatorgrouper.utils import remove_absent_students
from gatorgrouper.utils import read_student_file
from gatorgrouper.utils import group_creation
from gatorgrouper.utils import group_graph
from gatorgrouper.utils import display
from gatorgrouper.utils import constants


def run_arguments(GG_ARGUMENTS, preference=None):
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
    if GG_ARGUMENTS.method == constants.ALGORITHM_ROUND_ROBIN:
        GROUPED_STUDENT_IDENTIFIERS = group_creation.group_rrobin_num_group(
            SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.num_group
        )
    elif GG_ARGUMENTS.method == constants.ALGORITHM_GRAPH:
        GROUPED_STUDENT_IDENTIFIERS = group_graph.group_graph_partition(
            SHUFFLED_STUDENT_IDENTIFIERS,
            GG_ARGUMENTS.num_group,
            preferences=preference,
            preferences_weight=GG_ARGUMENTS.preferences_weight,
            preferences_weight_match=GG_ARGUMENTS.preferences_weight_match,
            objective_weights=GG_ARGUMENTS.objective_weights,
            objective_measures=GG_ARGUMENTS.objective_measures,
        )
    else:
        GROUPED_STUDENT_IDENTIFIERS = group_creation.group_random_num_group(
            SHUFFLED_STUDENT_IDENTIFIERS, GG_ARGUMENTS.num_group
        )
    return GROUPED_STUDENT_IDENTIFIERS
