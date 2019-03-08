"""Gather user Info"""

from .models import Professor, Semester_Class, Student
from django.db.models import Q

# given a professor and class, make a list of students
def gatherinfo(request):
    current_professor = request.user
    students = list(Semester_Class.objects.filter(professor_id = current_professor))
    return students

def gatherinfoConflict():
    listOfStudents = gatherinfo(request)
    conflicts = []
    for student in listOfStudents :
         conflicts.append(Student_Conflicts.object.filter(Q(student1 = student) | Q(student2 = student)))
    return conflicts
