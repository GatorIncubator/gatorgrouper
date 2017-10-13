from random import shuffle
import argparse
import itertools
import sys
#function files

def remove_absent_students(absentee_list, list_of_student_lists):
    list_of_student_lists_copy = list_of_student_lists[:]
    for name in absentee_list:
        for student_list in list_of_student_lists :
            if student_list[0] == name :
                list_of_student_lists_copy.remove(student_list)
    return list_of_student_lists_copy
