"""Gather user Info"""

from .models import Professor, Semester_Class, Student

# given a professor and class, make a list of students
def gatherinfo(request):
    current_professor = request.user
    students = list(Semester_Class.objects.filter(professor_id = current_professor))
