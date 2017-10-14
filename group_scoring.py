""" score groups by approximate level of diversity """

import itertools
from defaults import *
from shuffle_students import shuffle_students

def score_group(student_identifers, group_size):
    """ score single group """

    students_categories = []
    for student in student_identifers:
        students_categories.append(student.split(',')[1:])
    #print(students_categories)

    iterable = iter(student_identifers)
    student_groups = list(
        iter(lambda: list(itertools.islice(iterable, group_size)), []))
    last_group_index = len(student_groups) - 1
    if len(student_groups[last_group_index]) == SINGLETON_GROUP:
        receiving_group = student_groups[last_group_index - 1]
        too_small_group = student_groups[last_group_index]
        receiving_group.append(*too_small_group)
        student_groups.remove(too_small_group)

    good = 0
    for group in student_groups:
        score = 0
        for student in group:
            score += int(student.split(',')[1])
        print(score)
        print()
        if score == 0:
            group_students_categories(shuffle_students(student_identifers), group_size)
        if score >= group_size/2:
            good += 1
    print(good)
    print(student_groups)
    print()
    if good < (len(student_groups) * .5):
        group_students_categories(shuffle_students(student_identifers), group_size)
    return student_groups

def score_groups():
    """ score multiple groups """
