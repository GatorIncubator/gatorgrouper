""" This is undocumented """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Professor, Semester_Class, Student, Grouped_Student, Assignment


# Register your models here.

admin.site.register(Professor, UserAdmin)
admin.site.register(Semester_Class)
admin.site.register(Student)
admin.site.register(Grouped_Student)
admin.site.register(Assignment)
