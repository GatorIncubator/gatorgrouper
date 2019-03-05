""" This is undocumented """
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
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
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def create_group_from_csv(request):
    """ GET request displaying the CSV upload form"""
    pass
