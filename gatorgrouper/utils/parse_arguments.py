""" Parses command-line arguments """

import argparse
import logging
from gatorgrouper.utils import read_student_file
from gatorgrouper.utils import constants


from argparse import Namespace
from typing import List, Union


def parse_arguments(args: List[str]) -> Namespace:
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
        default=constants.DEFAULT_GRPSIZE,
        required=False,
    )

    gg_parser.add_argument(
        "--num-group",
        help="Number of groups",
        type=int,
        default=constants.DEFAULT_NUMGRP,
        required=False,
    )

    gg_parser.add_argument(
        "--file", required=True, type=str, help="Input the file path"
    )

    gg_parser.add_argument(
        "--method",
        type=str,
        help="Grouping algorithm",
        choices=[
            constants.ALGORITHM_GRAPH,
            constants.ALGORITHM_ROUND_ROBIN,
            constants.ALGORITHM_RANDOM,
        ],
        default=constants.DEFAULT_METHOD,
        required=False,
    )

    gg_parser.add_argument(
        "--absentees",
        help="Student that is absent",
        nargs="+",
        type=str,
        default=constants.DEFAULT_ABSENT,
        required=False,
    )

    gg_arguments_finished = gg_parser.parse_args(args)

    logging.basicConfig(
        format="%(levelname)s:%(pathname)s: %(message)s",
        level=gg_arguments_finished.logging_level,
    )
    return gg_arguments_finished


def check_valid_num_group(
    numgrp: int, students_list: Union[List[List[Union[str, bool]]], str]
) -> bool:
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


def check_valid_group_size(
    group_size: int, students_list: Union[List[List[Union[str, bool]]], str]
) -> bool:
    """ Checks if group size is valid """
    if students_list == "filenotfound":
        logging.info("Skipping group size check; file must not exist.")
        return True
    students_list_length = len(students_list)
    if args.group_size > 1 and args.group_size <= students_list_length / 2:
        verified_arguments = True
    if args.num_group > 1 and args.group_size <= students_list_length / 2:
        verified_arguments = True
    if args.file is constants.NONE:
        verified_arguments = False
    if read_student_file.read_csv_data(args.file) == "":
        verified_arguments = False
    return verified_arguments
