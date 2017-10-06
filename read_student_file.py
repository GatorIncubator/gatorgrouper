""" Reads the student identifies from the specific file,
        returning the identifiers in a list """

from random import shuffle
import argparse
import itertools
import sys


def read_student_file(students_file_name):
    with open(students_file_name, 'r') as students_file:
        student_identifers = [line.strip() for line in students_file]
    return student_identifers

