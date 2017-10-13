""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys
import logging
# default values
from defaults import *

def parse_gatorgrouper_arguments(args):
    """ Parses the arguments provided on the command-line """
    gg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    gg_parser.add_argument(
        "-d", "--debug",
        help="Display diagnostic information",
        action="store_const", dest="logging_level", const=logging.DEBUG, default=logging.ERROR
    )

    gg_parser.add_argument(
        "-v", "--verbose",
        help="Display confirmation information",
        action="store_const", dest="logging_level", const=logging.INFO
    )

    gg_parser.add_argument(
        "--group-size",
        help="Number of students in a group",
        type=int,
        default=DEFAULT_TEAM_SIZE,
        required=False)

    gg_parser.add_argument(
        "--students-file",
        help="File containing last name of students",
        type=str,
        default=DEFALT_STUDENT_FILE,
        required=False)

    gg_arguments_finished = gg_parser.parse_args(args)

    logging.basicConfig(format="%(levelname)s:%(pathname)s: %(message)s", level=gg_arguments_finished.logging_level)

    return gg_arguments_finished
