""" Parses command-line arguments """

import argparse
import logging
import read_student_file
import defaults
import constants


def parse_arguments(args):
    """ Parses the arguments provided on the command-line """

    gg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    gg_parser.add_argument(
        "-d",
        "--debug",
        help="Display diagnostic information",
        action="store_const",
        dest="logging_level",
        const=logging.DEBUG,
        default=logging.ERROR,
    )

    gg_parser.add_argument(
        "-v",
        "--verbose",
        help="Display confirmation information",
        action="store_const",
        dest="logging_level",
        const=logging.INFO,
    )

    gg_parser.add_argument(
        "--group-size",
        help="Number of students in a group",
        type=int,
        default=defaults.DEFAULT_GRPSIZE,
        required=False,
    )

    gg_parser.add_argument(
        "--num-group",
        help="Number of groups",
        type=int,
        default=defaults.DEFAULT_NUMGRP,
        required=False,
    )

    gg_parser.add_argument(
        "--students-file",
        help="File containing last name of students",
        type=str,
        default=defaults.DEFAULT_CSVFILE,
        required=False,
    )

    gg_parser.add_argument(
        "--random",
        help="Use random grouping method",
        action="store_const",
        dest="grouping_method",
        const="random",
    )

    gg_parser.add_argument(
        "--round-robin",
        help="Use round-robin grouping method",
        action="store_const",
        dest="grouping_method",
        const=constants.ALGORITHM_ROUND_ROBIN,
    )

    gg_parser.add_argument("--absentees", nargs="+", type=str)

    gg_arguments_finished = gg_parser.parse_args(args)

    logging.basicConfig(
        format="%(levelname)s:%(pathname)s: %(message)s",
        level=gg_arguments_finished.logging_level,
    )

    # pylint: disable=bad-continuation
    if (
        check_valid_group_size(
            gg_arguments_finished.group_size,
            read_student_file.read_student_file(gg_arguments_finished.students_file),
        )
        is False
    ):
        quit()

    if (
        check_valid_num_group(
            gg_arguments_finished.num_group,
            read_student_file.read_student_file(gg_arguments_finished.students_file),
        )
        is False
    ):
        quit()

    if gg_arguments_finished.absentees is None:
        gg_arguments_finished.absentees = []

    return gg_arguments_finished


def check_valid_num_group(numgrp, students_list):
    """Checking if valid num group"""
    if students_list == "filenotfound":
        logging.info("Skipping group size check; file must not exist.")
        return True
    students_list_length = len(students_list)
    if numgrp > students_list_length:
        logging.error("Number of groups: %d", numgrp)
        logging.error("Number of students: %d", students_list_length)
        logging.error(
            "Number of groups must be less than or equal to "
            "the number of students to be grouped. "
        )
        return False
    logging.info("Number of groups: %d", numgrp)
    logging.info("Number of students: %d", students_list_length)
    logging.info("Valid number of groups.")
    return True


def check_valid_group_size(group_size, students_list):
    """ Checks if group size is valid """
    if students_list == "filenotfound":
        logging.info("Skipping group size check; file must not exist.")
        return True
    students_list_length = len(students_list)
    if group_size <= 1 or group_size > students_list_length / 2:
        logging.error("Group size: %d", group_size)
        logging.error("Number of students: %d", students_list_length)
        logging.error(
            "Group size must be greater than 1 and less than "
            "or equal to half of the number of students."
        )
        return False
    # group size passed checks
    logging.info("Group size: %d", group_size)
    logging.info("Number of students: %d", students_list_length)
    logging.info("Valid group size.")
    return True
