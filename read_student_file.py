""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys

DEFALT_STUDENT_FILE = "students.txt"
GATORGROUPER_HOME = "GATORGROUPER_HOME"

DEFAULT_TEAM_SIZE = 2
SINGLETON_GROUP = 1


def read_student_file(students_file_name):
    """ Reads the student identifies from the specific file,
        returning the identifiers in a list """
    with open(students_file_name, 'r') as students_file:
        student_identifers = [line.strip() for line in students_file]
    return student_identifers

