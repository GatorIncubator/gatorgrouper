""" score groups by approximate level of diversity """

import itertools
from defaults import *
from group_random import *

def score_group(student_identifers, group_size):
    """ score single group """
    score = 0
    for student in student_identifers:
        for category in range(len(str(student).split(',')[1:])):
            print(student[category+1])
            if("True" in student[category+1]):
                score += 1
        print()
    print(score)
    return score

def score_groups(student_groups, group_size):
    """ score multiple groups """
    scores = []
    for group in student_groups:
        scores.append(score_group(group, group_size))
    if(0 in scores):
        print("Students not well distributed")
        print(scores.index(max(scores)))
        temp = max(student_groups[scores.index(max(scores))])
        lowest = min(student_groups[scores.index(min(scores))])
		
        student_groups[scores.index(max(scores))].insert(scores.index(max(scores)), lowest)
        student_groups[scores.index(max(scores))].remove(temp)
		
        student_groups[scores.index(min(scores))].insert(scores.index(min(scores)), temp)
        student_groups[scores.index(min(scores))].remove(lowest)
        score_groups(student_groups, group_size)
	