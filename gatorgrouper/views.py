""" This is undocumented """
import csv
from io import StringIO
from django.shortcuts import render
from .utils.group_creation import group_rrobin_num_group
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
    return render(request, "gatorgrouper/classes.html", {"title": "Create Classes"})
    # return HttpResponse


def assignments(request):
    """ Create assignments view """
    return render(
        request, "gatorgrouper/assignments.html", {"title": "Create Assignments"}
    )


def survey(request):
    """ Student's grouping preference? """
    return render(request, "gatorgrouper/survey.html", {"title": "Survey"})


def groupResult(request):
    """ Group result view """
    return render(
        request, "gatorgrouper/viewing-groups.html", {"title": "Group Result"}
    )
