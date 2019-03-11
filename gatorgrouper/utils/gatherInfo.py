"""Gather user Info"""

from django.db.models import Q
# pylint: disable=no-name-in-module
from gatorgrouper.models import Student, Student_Conflict  # pylint: disable=import-error


# given a professor and class, make a list of students
def gatherStudents(current_class):
    """ gathers list of students in given class """
    students = list(Student.objects.filter(class_id=current_class))
    return students


def gatherConflicts(current_class):
    """ Gathers student conflict info """
    listOfStudents = gatherStudents(current_class)
    conflicts = []
    for student in listOfStudents:
        conflicts.append(
            Student_Conflict.object.filter(Q(student1=student) | Q(student2=student))
        )
    return conflicts
