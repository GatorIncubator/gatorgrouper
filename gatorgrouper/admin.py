""" This is undocumented """
from django.contrib import admin
from .models import Professor, Semester_Class, Students, Grouped_Students, Assignments
from .models import Student_Conflicts

# Register your models here.

admin.site.register(Professor)
admin.site.register(Semester_Class)
admin.site.register(Students)
admin.site.register(Grouped_Students)
admin.site.register(Assignments)
admin.site.register(Student_Conflicts)
