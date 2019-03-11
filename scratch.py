""" This is undocumented """
import csv
from io import StringIO
from django.shortcuts import render
from django.http import Http404
from .utils.group_rrobin import group_rrobin_num_group
from .forms import UploadCSVForm, StudentCompatibilityFormSet
from .models import Semester_Class


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
    return render(request, "gatorgrouper/assignments.html", {"form": form})


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
    return render(request, "gatorgrouper/home.html")
    # return HttpResponse


def create_classes(request):
    """ Create classes view """
    return render(request, "gatorgrouper/chttps://docs.djangoproject.com/en/2.1/ref/databases/lasses.html", {"title": "Create Classes"})
    # return HttpResponse


def assignments(request):
    """ Create assignments view """
    return render(
        request, "gatorgrouper/assignments.html", {"title": "Create Assignments"}
    )

def users(request):
    """ Create user view"""
    return render( request)

def survey(request, class_id = None):
    """ POST and GET requests for handling student survey """
    # TODO: get students in class
    # TODO: make formset with a compatibility form for each student
    # TODO: populate formset with existing compatibility responses
    # TODO: validate formset
    # TODO: save to db

    # Verify that the class exists
    try:
        Semester_Class.objects.get(class_id = class_id)
    except Semester_Class.DoesNotExist:
        raise Http404("Class not found")
    enrolled_students = Students.objects.filter(class_id = class_id)
    if request.method == "POST":
        formset = StudentCompatibilityFormSet(request.POST)
        if formset.is_valid():
            print(formset.cleaned_data)
            return render(request, "gatorgrouper/survey.html")
    else:
        # TODO: ensure logged in user is enrolled as student
        formset = StudentCompatibilityFormSet()
    print(formset)
    return render(request, "gatorgrouper/survey.html", {"form": formset})


def groupResult(request):
    """ Group result view """
    return render(
        request, "gatorgrouper/viewing-groups.html", {"title": "Group Result"}
    )
