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


def upload_csv(request):
    """ POST request for handling CSV upload and grouping students """
    pass
