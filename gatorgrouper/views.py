""" This is undocumented """
import csv
from io import StringIO
from django.shortcuts import render, redirect
from django.template import loader
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse
# from django.http import Http404
from .models import Professor, Semester_Class, Student
from .models import Assignment, Grouped_Student

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
def index(request):
    """ This is undocumented """
    current_professor = request.user
    classes = list(Semester_Class.objects.filter(professor_id=current_professor))
    assignments = list(Assignment.objects.all())
    for item in classes:
        print(item)
    return render(
        request,
        "gatorgrouper/index.html",
        {"all_classes": classes, "all_assignments": assignments},
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
    if request.user.__str__() != "AnonymousUser":
        print(request.user.email)
        print("Hello")
    return render(request, "gatorgrouper/home.html")
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

            return redirect("Gatorgrouper-home")
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
        Assignment, fields=("class_id", "assignment_id", "description")
    )
    if request.method == "POST":
        formset = AssignmentFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("Gatorgrouper-home")
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
