""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys

DEFALT_STUDENT_FILE = "students.txt"
GATORGROUPER_HOME = "GATORGROUPER_HOME"

DEFAULT_TEAM_SIZE = 2
SINGLETON_GROUP = 1


def display_diagnostics(student_identifers, student_groups):
    """ Display information about what was generated """
    print("Successfully placed",
          len(student_identifers), "students into",
          len(student_groups), "groups")
    print()

