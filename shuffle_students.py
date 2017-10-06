""" Shuffle the student identifiers """

from random import shuffle
import argparse
import itertools
import sys


def shuffle_students(student_identifers):
    shuffled_student_identifers = student_identifers[:]
    shuffle(shuffled_student_identifers)
    return shuffled_student_identifers

