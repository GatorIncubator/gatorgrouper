""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys

def create_escaped_string_from_list(student_identifers):
    """ Return a string that lists the student identifiers """
    student_list = ""
    for student in student_identifers:
        student_list = student_list + student + "\n"
    return student_list
