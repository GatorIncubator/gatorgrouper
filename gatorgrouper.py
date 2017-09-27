""" GatorGrouper randomly assigns a list of students to a group """

import os
import sys

import argparse

DEFALT_STUDENT_FILE = "students.txt"
DEFAULT_TEAM_SIZE = 2
GATORGROUPER_HOME = "GATORGROUPER_HOME"
SLASH = "/"

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

    gg_parser.add_argument(
        "--student-file",
        help="File containing last name of students",
        type=str,
        default=DEFALT_STUDENT_FILE,
        required=False)

    gg_arguments_finished = gg_parser.parse_args(args)
    return gg_arguments_finished


def display_welcome_message():
    """ Display a welcome message """
    print()
    print(
        "GatorGrouper: Automatically Assign Students to Groups"
    )
    print("https://github.com/gkapfham/gatorgrouper")
    print()


if __name__ == '__main__':
    # parse the arguments and display welcome message
    gg_arguments = parse_gatorgrader_arguments(sys.argv[1:])
    display_welcome_message()
    if gg_arguments.verbose is True:
        print("Configuration of GatorGrouper:")
        print(gg_arguments)
        print()
