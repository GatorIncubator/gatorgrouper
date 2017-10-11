""" GatorGrouper randomly assigns a list of students to groups """
"""Issue #2"""

from random import shuffle
import argparse
import itertools
import sys
#default values
from defaults import *


def parse_gatorgrader_arguments(args):
    """ Parses the arguments provided on the command-line """
    gg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    gg_parser.add_argument(
        "--verbose",
        help="Display verbose diagnostic information",
        action="store_true")

    gg_parser.add_argument(
        "--group-size",
        help="Number of students in a group",
        type=int,
        default=DEFAULT_TEAM_SIZE,
        required=False)
        if len(student_identifers) > 1 and gg_arguments.group_size < (len(student_identifers)/2):
            print("Invalid arguments")
            quit()

    gg_parser.add_argument(
        "--students-file",
        help="File containing last name of students",
        type=str,
        default=DEFAULT_STUDENT_FILE,
        required=False)

    # Arguments for number of groups if needed
    #gg_parser.add_argument(
    #    "--number-of-group",
    #    help="Number of groups",
    #    type=int,
    #    required=False)

    gg_arguments_finished = gg_parser.parse_args(args)

    return gg_arguments_finished
