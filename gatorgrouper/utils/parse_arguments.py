""" Parses command-line arguments """

import argparse
import logging
from gatorgrouper.utils import read_student_file
from gatorgrouper.utils import constants


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


def check_valid(args, students_list):
    """Verify the command-line arguments"""
    verified_arguments = False
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
