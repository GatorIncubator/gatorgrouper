"""Gather user Info"""

from django.db.models import Q

from gatorgrouper.models import Student, Student_Conflict


# given a professor and class, make a list of students
def gatherStudents(current_class):
    """ gathers list of students in given class """
    # pylint: disable=no-member
    students = list(Student.objects.filter(class_id=current_class))
    student_list = {}
    for student in students:
        student_list[
            student.first_name + " " + student.last_name,
        ] = student  # noqa: E231
    return student_list


def gatherConflicts(current_class):
    """ Gathers student conflict info """
    listOfStudents = gatherStudents(current_class)
    conflicts = []
    for student in listOfStudents:
        conflicts.append(
            # pylint: disable=no-member
            Student_Conflict.object.filter(Q(student1=student) | Q(student2=student))
        )
    return conflicts
