""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys


def display_student_identifiers(student_identifers):
    """ Display the student identifiers """
    for student in student_identifers:
        print(student)

