""" This is undocumented """
from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
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
    return render(request, 'gatorgrouper/home.html')
    # return HttpResponse('<h1>Blog Home</h1>')

def classes(request):
    return render(request, 'gatorgrouper/classes.html', {'title': 'Create Classes'})
    # return HttpResponse('<h1>Blog Picture</h1>')

def assignments(request):
    return render(request, 'gatorgrouper/assignments.html', {'title': 'Create Assignments'})

def survey(request):
    return render(request, 'gatorgrouper/survey.html', {'title': 'Survey'})

def signup(request):
    return render(request, 'gatorgrouper/signup.html', {'title': 'Signup'})

def groupResult(request):
    return render(request, 'gatorgrouper/viewing-groups.html', {'title': 'Group Result'})
