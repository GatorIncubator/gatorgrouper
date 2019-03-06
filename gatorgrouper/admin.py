""" This is undocumented """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Professor, Semester_Class, Students, Grouped_Students, Assignments


# Register your models here.

admin.site.register(Professor, UserAdmin)
admin.site.register(Semester_Class)
admin.site.register(Students)
admin.site.register(Grouped_Students)
admin.site.register(Assignments)
