""" This file allows us to write our own custom views for our HTML templates"""
import csv
import re
from io import StringIO
from django.shortcuts import render, redirect
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.views.generic import DetailView
from django.utils.decorators import method_decorator

from .models import Semester_Class, Student
from .models import Grouped_Student, Assignment
from .utils.gatherInfo import gatherStudents
from .utils.run import input_interface
from .utils import constants
from .forms import UploadCSVForm, CreateGroupForm
from .forms import CustomUserCreationForm
from .forms import AssignmentForm, StudentForm, GroupForm


# pylint: disable=too-many-ancestors
@method_decorator(login_required, name="dispatch")
class AssignmentView(DetailView):
    """ This view allows there to be a unique page for each assignment
    it passes information to the template to customize each assignment page"""

    model = Assignment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.object
        group_list = list(
            # pylint: disable=no-member
            Grouped_Student.objects.filter(assignment_id=instance).order_by(
                "group_name"
            )
        )
        groupNames = []
        for g in group_list:
            if g.group_name not in groupNames:
                groupNames.append(g.group_name)

        context["groups"] = group_list
        context["groupNames"] = groupNames

        return context


# Collects information from the form and passes it to upload_csv.html
def upload_csv(request):
    """ POST request for handling CSV upload and grouping students """
    if request.method == "POST":
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            responses = parse_uploaded_csv(request.FILES["student_data"])
            if request.FILES.get("student_preferences"):
                preferences = parse_uploaded_csv(
                    request.FILES["student_preferences"], as_dict=True
                )
            else:
                preferences = None
            numgrp = form.cleaned_data["numgrp"]
            preferences_weight = form.cleaned_data["preferences_weight"]
            preferences_weight_match = form.cleaned_data["preferences_weight_match"]
            groups = input_interface(
                responses,
                method=constants.ALGORITHM_GRAPH,
                num_group=numgrp,
                preferences=preferences,
                preferences_weight=preferences_weight,
                preferences_weight_match=preferences_weight_match,
            )
            return render(
                request, "gatorgrouper/viewing-groups-csv.html", {"groups": groups}
            )
    else:
        form = UploadCSVForm()
    return render(request, "gatorgrouper/upload_csv.html", {"form": form})


def parse_uploaded_csv(csvfile, as_dict=False):
    """
        Transform uploded CSV data into list of student responses:
        [["student name", True, False, ...], ...]

        With the as_dict parameter set to True, transforms the CSV data into a dictionary of sets:
        {"student name": {True, False, ...}, ...}
    """
    f = StringIO(csvfile.read().decode("utf-8"))
    csvdata = list(csv.reader(f, delimiter=","))

    # transform into desired output
    responses = list()
    responses_dict = {}
    for record in csvdata:
        if as_dict:
            # Create key in responses dictionary
            responses_dict[record[0]] = set()
        temp = list()
        temp.append(record[0].replace('"', ""))
        for value in record[1:]:
            if value.lower() == "true":
                temp.append(True)
            elif value.lower() == "false":
                temp.append(False)
            # pylint: disable=bad-continuation
            elif re.match(r"[+-]?([0-9]*[.])?[0-9]+", value):
                # Match a float with regex
                temp.append(float(value))
            else:
                # Keep the value as a string if no other type matches
                temp.append(value)
            if as_dict:  # Assign the value to the responses set for this row
                responses_dict[record[0]].add(value)
        responses.append(temp)
    return responses if not as_dict else responses_dict


def register(request):
    """ This view loads the register page and handles the form """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            # message = "Account created for " + first_name + " " + last_name
            # messages.success(request, message=message)
            messages.success(request, f"Account created for {first_name} {last_name}")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(
        request, "gatorgrouper/register.html", {"title": "Register", "form": form}
    )


# Collects information regarding the Professor, classes, assignment_list, and Students
# and passes it to profile.html
@login_required
def profile(request):
    """ Loads the user in correspondence through the professor and Returns
        a list of the classes, assignments, and students related to it """
    current_professor = request.user
    # pylint: disable=no-member
    classes = list(Semester_Class.objects.filter(professor_id=current_professor))
    # pylint: disable=no-member
    assignment_list = list(Assignment.objects.all())
    # pylint: disable=no-member
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
    # get rid of decode because it's already default in python3
    # f = StringIO(csvfile.read().decode("utf-8"))
    f = StringIO(csvfile.read())
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


# Returns the user to the home page
def home(request):
    """ Homepage view """

    return render(request, "gatorgrouper/home.html", {"title": "Home"})
    # return HttpResponse


# Function to view the list of classes provided by the Professor and passed to
# classes.html
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


# Allows the user to view the list of assignments
@login_required
def assignments(request):
    """ Create assignments view """
    if request.method == "POST":
        formset = AssignmentForm(request.user, request.POST)
        if formset.is_valid():
            stock = formset.save(commit=False)
            stock.professor_id = request.user
            stock.save()
            messages.success(request, f"Assignment Successfully Created")
            return redirect("profile")
    else:
        formset = AssignmentForm(request.user)

    return render(
        request,
        "gatorgrouper/assignments.html",
        {"title": "Create Assignments", "formset": formset},
    )


# Using the survey to get the grouping preference for the students
@login_required
def survey(request):
    """ Student's grouping preference? """
    return render(request, "gatorgrouper/survey.html", {"title": "Survey"})


# Function allows displaying current students and add students based on the request
@login_required
def add_students(request):
    """ Used to display current students in roster and provides option to add students """
    if request.method == "POST":
        formset = StudentForm(request.user, request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, f"Student Successfully Created")
            return redirect("add-students")
    else:
        formset = StudentForm(request.user)
    return render(
        request,
        "gatorgrouper/add-students.html",
        {"title": "Add a Student", "formset": formset},
    )


# Allows to create a group using the rrobin method
# pylint: disable=too-many-locals
@login_required
def create_groups(request):
    """ Finds all the required information, call GatorGrouper with the provided
       information and displays it to the user and saves it if clicked 'save' """
    groups = []
    if not request.user.is_authenticated:
        return redirect("upload-csv")
    # pylint: disable=too-many-nested-blocks
    # conditional logic for a 'POST' request
    if request.method == "POST":
        formset = GroupForm(request.user, request.POST)
        groupNum = CreateGroupForm(request.POST)
        # Conditional logic to see if the submitted forms are valid
        if groupNum.is_valid() and formset.is_valid():
            assignment_obj = formset.cleaned_data.get("assignment_id")
            class_id_num = assignment_obj.class_id.class_id
            num_of_groups = groupNum.cleaned_data.get("numgrp")
            student_list_dict = gatherStudents(class_id_num)
            # pylint: disable=unused-variable
            # Dictionary to hold student object and student names and returns
            # the dictionary
            student_list = []
            # Finds the student object based on the student name and finds the assignment id
            for name, obj in student_list_dict.items():
                student_list.append(name)
            groups = input_interface(
                student_list, constants.ALGORITHM_ROUND_ROBIN, num_of_groups
            )
            if request.POST["button"] == "save":
                counter = 1
                for group in groups:
                    group_name = "Group " + str(counter)
                    # For loop to go through each student in the group and saves
                    # each student with the required information
                    for student in group:
                        try:
                            s = Grouped_Student(
                                assignment_id=assignment_obj,
                                student_id=student_list_dict[student],
                                group_name=group_name,
                            )
                            # Saving all the above information
                            s.save()
                        # To check if the assignment_id and student_id hold unique
                        # values. If not, send error message
                        except IntegrityError:
                            messages.error(
                                request,
                                f"This assignment already has a group associated "
                                + f"with it.\nPlease Try again",
                            )
                            return redirect("create-groups")
                    # Successful message sent once it puts every student and every
                    # group inside the database
                    counter += 1
                messages.success(
                    request,
                    f"The groups for this assignment have been saved. To see them,"
                    + f"visit the view groups page",
                )
    # condition to pass the empty form at the beginning
    else:
        formset = GroupForm(request.user)
        groupNum = CreateGroupForm()

    return render(
        request,
        "gatorgrouper/create-groups.html",
        {
            "title": "Create Groups",
            "formset": formset,
            "group_list": groups,
            "groupNum": groupNum,
        },
    )
