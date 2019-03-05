""" This is undocumented """
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadCSVForm
from .models import Professor, Semester_Class
from io import StringIO
import csv


# Create your views here.
def index(request):
    """ This is undocumented """
    professors = Professor.objects.all()
    classes = Semester_Class.objects.all()

    # pylint: disable=unused-variable
    template = loader.get_template("gatorgrouper/index.html")  # noqa: F841

    return render(
        request,
        "gatorgrouper/index.html",
        {"all_professors": professors, "all_classes": classes},
    )


def upload_csv(request):
    """ POST request for handling CSV upload and grouping students """
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            responses = handle_uploaded_file(request.FILES['file'])
            print(responses)
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadCSVForm()
    return render(request, 'upload.html', {'form': form})


def create_group_from_csv(request):
    """ GET request displaying the CSV upload form"""
    pass

def handle_uploaded_file(csvfile):
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
