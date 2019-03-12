""" This is undocumented """
import csv
from io import StringIO
from django.shortcuts import render, redirect
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm


# from django.http import HttpResponse
# from django.http import Http404
from .models import Semester_Class, Student
from .models import Assignment
from .utils.gatherInfo import gatherStudents

from .utils.group_rrobin import group_rrobin_num_group
from .forms import UploadCSVForm


def upload_csv(request):
    """ POST request for handling CSV upload and grouping students """
    if request.method == "POST":
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            responses = handle_uploaded_file(request.FILES["file"])
            numgrp = form.cleaned_data["numgrp"]
            groups = group_rrobin_num_group(responses, numgrp)
            return render(
                request, "gatorgrouper/viewing-groups.html", {"groups": groups}
            )
    else:
        form = UploadCSVForm()
    return render(request, "gatorgrouper/upload_csv.html", {"form": form})


# Create your views here.
def register(request):
    """ This view loads the register page and handles the form """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            messages.success(request, f"Account created for {first_name} {last_name}")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(
        request, "gatorgrouper/register.html", {"title": "Register", "form": form}
    )


@login_required
def profile(request):
    """ This is undocumented """
    current_professor = request.user
    classes = list(Semester_Class.objects.filter(professor_id=current_professor))
    assignment_list = list(Assignment.objects.all())
    students = list(Student.objects.all())
    return render(
        request,
        "gatorgrouper/profile.html",
        {
            "title": "Profile",
            "all_classes": classes,
            "all_assignments": assignment_list,
            "all_students": students,
        },
    )


def handle_uploaded_file(csvfile):
    """
        Transform uploded CSV data into list of student responses:
        [["student name", True, False, ...]]
    """
    f = StringIO(csvfile.read().decode("utf-8"))
    csvdata = list(csv.reader(f, delimiter=","))

    # transform into desired output
    responses = list()
    for record in csvdata:
        temp = list()
        temp.append(record[0].replace('"', ""))
        for value in record[1:]:
            if value.lower() == "true":
                temp.append(True)
            elif value.lower() == "false":
                temp.append(False)
        responses.append(temp)
    return responses


def home(request):
    """ Homepage view """

    return render(request, "gatorgrouper/home.html", {"title": "Home"})
    # return HttpResponse


@login_required
def create_classes(request):
    """ Create classes view """

    ClassFormSet = modelform_factory(
        Semester_Class,
        fields=("semester", "department", "class_number", "class_section"),
    )
    if request.method == "POST":
        formset = ClassFormSet(request.POST)
        if formset.is_valid():
            stock = formset.save(commit=False)
            stock.professor_id = request.user
            stock.save()
            messages.success(request, f"Class Added")
            return redirect("profile")
    else:
        formset = ClassFormSet()

    return render(
        request,
        "gatorgrouper/classes.html",
        {"title": "Create Classes", "formset": formset},
    )
    # return HttpResponse


@login_required
def assignments(request):
    """ Create assignments view """
    AssignmentFormSet = modelform_factory(
        Assignment, fields=("class_id", "assignment_name", "description")
    )
    if request.method == "POST":
        formset = AssignmentFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, f"Assignment Successfully Created")
            return redirect("profile")
    else:
        formset = AssignmentFormSet()

    return render(
        request,
        "gatorgrouper/assignments.html",
        {"title": "Create Assignments", "formset": formset},
    )


@login_required
def survey(request):
    """ Student's grouping preference? """
    return render(request, "gatorgrouper/survey.html", {"title": "Survey"})


@login_required
def groupResult(request):
    """ Group result view """
    return render(
        request, "gatorgrouper/viewing-groups.html", {"title": "Group Result"}
    )


@login_required
def add_students(request):
    """ Used to display current students in roster and provides option to add students """
    StudentFormSet = modelform_factory(
        Student, fields=("class_id", "first_name", "last_name")
    )
    if request.method == "POST":
        formset = StudentFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, f"Student Successfully Created")
            return redirect("add-students")
    else:
        formset = StudentFormSet()
    return render(
        request,
        "gatorgrouper/add-students.html",
        {"title": "Add a Student", "formset": formset},
    )


@login_required
def create_groups(request):
    """ Created groups using gatorgrouper functions """
    AssignmentFormSet = modelform_factory(
        Assignment, fields=("class_id", "assignment_id")
    )
    if request.method == "POST":
        formset = AssignmentFormSet(request.POST)
        if formset.is_valid():
            class_id_num = formset.cleaned_data.get("class_id")
            student_list = gatherStudents(class_id_num)
            for student in student_list:
                print(student)
    else:
        formset = AssignmentFormSet(request.POST)
    # conflict_list = gatherConflicts(request)

    # don't forget to import gatherConflicts and Grouped_students,
    # removed those imports for flake8 test
    return render(
        request,
        "gatorgrouper/create-groups.html",
        {"title": "Create Groups", "formset": formset},
    )
