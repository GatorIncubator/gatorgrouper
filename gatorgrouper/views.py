from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from .models import Professor, Semester_Class

# Create your views here.
def index(request):
    professors = Professor.objects.all()
    classes = Semester_Class.objects.all()

    template = loader.get_template("gatorgrouper/index.html")

    return render(
        request,
        "gatorgrouper/index.html",
        {"all_professors": professors, "all_classes": classes},
    )
