""" This is undocumented """
import csv
import re
from io import StringIO
from django.shortcuts import render
from .utils.group_graph import group_graph_partition
from .forms import UploadCSVForm


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
            groups = group_graph_partition(responses, numgrp, preferences=preferences)
            return render(
                request, "gatorgrouper/viewing-groups.html", {"groups": groups}
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
            responses_dict[record[0]] = set()  # Create key in responses dictionary
        temp = list()
        temp.append(record[0].replace('"', ""))
        for value in record[1:]:
            if value.lower() == "true":
                temp.append(True)
            elif value.lower() == "false":
                temp.append(False)
            elif re.match(
                r"[+-]?([0-9]*[.])?[0-9]+", value  # pylint: disable=bad-continuation
            ):  # Match a float with regex
                temp.append(float(value))
            else:  # Keep the value as a string if no other type matches
                temp.append(value)
            if as_dict:  # Assign the value to the responses set for this row
                responses_dict[record[0]].add(value)
        responses.append(temp)
    return responses if not as_dict else responses_dict


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
