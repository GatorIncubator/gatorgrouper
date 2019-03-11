"""Gather user Info"""

from gatorgrouper.models import Professor, Semester_Class, Student
from django.db.models import Q

# given a professor and class, make a list of students
def gatherStudents(current_class):
    students = list(Student.objects.filter(class_id = current_class))
    return students

def gatherConflicts():
    listOfStudents = gatherStudents(request)
    conflicts = []
    for student in listOfStudents :
         conflicts.append(Student_Conflicts.object.filter(Q(student1 = student) | Q(student2 = student)))
    return conflicts
