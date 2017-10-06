""" Display information about what was generated """

from random import shuffle
import argparse
import itertools
import sys


def display_diagnostics(student_identifers, student_groups):
    print("Successfully placed",
          len(student_identifers), "students into",
          len(student_groups), "groups")
    print()

