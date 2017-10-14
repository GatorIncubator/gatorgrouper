""" Parses the arguments provided on the command-line """

from random import shuffle
import argparse
import itertools
import sys
import logging
#default values
from defaults import *
from read_student_file import read_student_file

def parse_gatorgrouper_arguments(args):

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
        default=DEFAULT_STUDENT_FILE,
        required=False)

    gg_arguments_finished = gg_parser.parse_args(args)

    logging.basicConfig(format="%(levelname)s:%(pathname)s: %(message)s", level=gg_arguments_finished.logging_level)

    if check_valid_group_size(gg_arguments_finished.group_size, gg_arguments_finished.students_file) == False:
        quit()

    return gg_arguments_finished

def check_valid_group_size(group_size, students_file_name):
    student_list = read_student_file(students_file_name)
    student_list_length = len(student_list)
    if (group_size <= 1 or group_size > student_list_length / 2): # indicates invalid group size
        logging.error("Group size: " + str(group_size) + "\nNumber of students: " + str(student_list_length) + "\nGroup size must be greater than 1 and less than or equal to half of the number of students.")
        return False
    else:
        logging.info("Group size: " + str(group_size) + "\nNumber of students: " + str(student_list_length) + "\nValid group size.")
        return True
