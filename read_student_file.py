""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle
import argparse
import itertools
import sys

size = 0

def read_student_file(students_file_name):
    """ Reads the student identifies from the specific file,
        returning the identifiers in a list """
    with open(students_file_name, 'r') as students_file:
        student_identifers = [line.strip() for line in students_file]
    size = len(student_identifers)
    return student_identifers

def student_list_length():
    """ Returns the number of students in the 
        list of student_identifiers """
    return size
