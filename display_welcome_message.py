""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys

DEFALT_STUDENT_FILE = "students.txt"
GATORGROUPER_HOME = "GATORGROUPER_HOME"

DEFAULT_TEAM_SIZE = 2
SINGLETON_GROUP = 1


def display_welcome_message():
    """ Display a welcome message """
    print()
    print("GatorGrouper: Automatically Assign Students to Groups")
    print("https://github.com/gkapfham/gatorgrouper")
    print()

