from random import shuffle
import argparse
import itertools
import sys
#default values
from defaults import *

def group_students_categories(student_identifers, group_size):
	students_categories = []
	for student in student_identifers:
		students_categories.append(student.split(',')[1:])
	print(students_categories)
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
		if(score == group_size):
			good += 1
		#if(score == 0):
			#group_students_categories(student_identifers, group_size)
		#print(str(score))
	print(str(good))
	print(str((group_size * .5)))
	if(good < (group_size * .5)):
		group_students_categories(student_identifers, group_size)
	return student_groups