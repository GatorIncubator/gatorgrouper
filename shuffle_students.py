""" Shuffle the student identifiers """

from random import shuffle
import argparse
import itertools
import sys


def shuffle_students(student_identifiers):
    shuffled_student_identifiers = student_identifiers[:]
    shuffle(shuffled_student_identifiers)
    return shuffled_student_identifiers

