""" Run all arguments which were passed in to main program """

import logging

from gatorgrouper.utils import remove_absent_students
from gatorgrouper.utils import read_student_file
from gatorgrouper.utils import group_creation
from gatorgrouper.utils import group_graph
from gatorgrouper.utils import display
from gatorgrouper.utils import constants


def run_arguments(GG_ARGUMENTS, preference=None):
    """ Run different algorithms with input arguments """
    STUDENT_IDENTIFIERS = remove_absent_students.remove_missing_students(
        GG_ARGUMENTS.absentees, read_student_file.read_csv_data(GG_ARGUMENTS.file)
    )
    logging.info("GatorGrouper will group these students:")
    logging.info("\n %s", display.create_escaped_string_from_list(STUDENT_IDENTIFIERS))

    # shuffle the student identifiers
    SHUFFLED_STUDENT_IDENTIFIERS = group_creation.shuffle_students(STUDENT_IDENTIFIERS)
    logging.info("GatorGrouper randomly ordered the students:")
    logging.info(
        "\n %s", display.create_escaped_string_from_list(SHUFFLED_STUDENT_IDENTIFIERS)
    )

    GROUPED_STUDENTS = input_interface(
        students=SHUFFLED_STUDENT_IDENTIFIERS,
        method=GG_ARGUMENTS.method,
        num_group=GG_ARGUMENTS.num_group,
        preferences=preference,
        preferences_weight=GG_ARGUMENTS.preferences_weight,
        preferences_weight_match=GG_ARGUMENTS.preferences_weight_match,
        objective_weights=GG_ARGUMENTS.objective_weights,
        objective_measures=GG_ARGUMENTS.objective_measures,
    )

    return GROUPED_STUDENTS


# pylint: disable=bad-continuation,too-many-arguments
def input_interface(
    students,
    method=None,
    num_group=None,
    preferences=None,
    preferences_weight=None,
    preferences_weight_match=None,
    objective_weights=None,
    objective_measures=None,
):
    """ Run conditional logic statment to ran different methods """
    students_reshuffle = group_creation.shuffle_students(students)
    if method == constants.ALGORITHM_ROUND_ROBIN:
        # Note that this only checks the first student
        if len(students_reshuffle[0]) < 2:
            grouped_students = group_creation.group_random_num_group(
                students_reshuffle, num_group
            )
        else:
            grouped_students = group_creation.group_rrobin_num_group(
                students_reshuffle, num_group
            )
    elif method == constants.ALGORITHM_GRAPH:
        grouped_students = group_graph.group_graph_partition(
            students_reshuffle,
            num_group,
            preferences=preferences,
            preferences_weight=preferences_weight,
            preferences_weight_match=preferences_weight_match,
            objective_weights=objective_weights,
            objective_measures=objective_measures,
        )
    else:
        grouped_students = group_creation.group_random_num_group(
            students_reshuffle, num_group
        )
    return grouped_students
