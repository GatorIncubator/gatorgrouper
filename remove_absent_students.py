from random import shuffle
import argparse
import itertools
import sys
#function files
from parse_gatorgrader_arguments import parse_gatorgrader_arguments
from read_student_file import read_student_file
from display_diagnostics import display_diagnostics
from display_student_identifiers import display_student_identifiers
from display_student_groups import display_student_groups
from shuffle_students import shuffle_students
from group_students import group_students
from display_welcome_message import display_welcome_message
from gatorgrouper import gatorgrouper

def remove_absent_students():
    absent = rawinput("Are any students absent? yes or no")
    if absent = 'yes':
