""" This is undocumented """
import csv
from io import StringIO
from django.shortcuts import render
from django.http import Http404
from .utils.group_rrobin import group_rrobin_num_group
from .forms import UploadCSVForm, StudentCompatibilityFormSet
from .models import Semester_Class
from .models import Student_Reviews


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


def survey(request, class_id = None):
    """ POST and GET requests for handling student survey """
    
    # Verify that the class exists
    try:
        Semester_Class.objects.get(class_id = class_id)
    except Semester_Class.DoesNotExist:
        raise Http404("Class not found")
    
    # get students in class
    enrolled_students = Students.objects.filter(class_id = class_id)
    
    # make formset with a compatibility form for each student
    if request.method == "POST":
        formset = StudentCompatibilityFormSet(request.POST)
    
        # validate formset
        if formset.is_valid():
            # TODO: populate formset with existing compatibility responses
            student_reviews = Student_Reviews()
            
            student_reviews.option1 = formset.cleaned_data['option1']
            student_reviews.option2 = formset.cleaned_data['option2']
            student_reviews.option3 = formset.cleaned_data['option3']
            student_reviews.option4 = formset.cleaned_data['option4']
            student_reviews.option5 = formset.cleaned_data['option5']

            print(formset.cleaned_data)
            # TODO: save to db
            student_reviews.save() 
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
