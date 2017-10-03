""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys

DEFALT_STUDENT_FILE = "students.txt"
GATORGROUPER_HOME = "GATORGROUPER_HOME"

DEFAULT_TEAM_SIZE = 2
SINGLETON_GROUP = 1


def display_student_groups(student_groups):
    """ Display the student groups with labels """
    group_counter = 1
    for student_group in student_groups:
        print("Group", group_counter)
        print(*student_group)
        print()
        group_counter = group_counter + 1

