""" This is undocumented """
from django.shortcuts import render
from django.template import loader

# from django.http import HttpResponse
# from django.http import Http404
from .models import Professor, Semester_Class


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
