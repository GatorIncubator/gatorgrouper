""" GatorGrouper randomly assigns a list of students to groups """

from random import shuffle


def shuffle_students(student_identifers):
    """ Shuffle the student identifiers """
    shuffled_student_identifers = student_identifers[:]
    shuffle(shuffled_student_identifers)
    return shuffled_student_identifers
