""" This is undocumented """
from django.shortcuts import render, redirect
from django.template import loader
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages


# from django.http import HttpResponse
# from django.http import Http404
from .models import Professor, Semester_Class, Student
from .models import Assignment, Grouped_Student


# Create your views here.
def register(request):
    """ This view loads the register page and handles the form """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'Account created for {first_name} {last_name}')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, "gatorgrouper/register.html", {"title": "Register",'form':form})


@login_required
def profile(request):
    """ This is undocumented """
    current_professor = request.user
    classes = list(Semester_Class.objects.filter(professor_id = current_professor))
    assignments = list(Assignment.objects.all())
    students = list(Student.objects.all())
    for item in classes:
        print(item)
    return render(
        request,
        "gatorgrouper/profile.html",
        {"title": "Profile", "all_classes": classes, "all_assignments": assignments, "all_students": students },
    )


def home(request):
    """ Homepage view """
    if request.user.__str__() != 'AnonymousUser':
        print(request.user.email)
        print("Hello")
    return render(request, "gatorgrouper/home.html", {"title": "Home"})
    # return HttpResponse


@login_required
def create_classes(request):
    """ Create classes view """

    ClassFormSet = modelform_factory(Semester_Class, fields=("semester","department","class_number","class_section"))
    if request.method == "POST":
        formset = ClassFormSet(request.POST)
        if formset.is_valid():
            stock = formset.save(commit=False)
            stock.professor_id = request.user
            stock.save()
            messages.success(request, f'Class Added')
            return redirect('profile')
    else:
        formset = ClassFormSet()

    return render(request, "gatorgrouper/classes.html", {"title": "Create Classes",'formset': formset})
    # return HttpResponse


@login_required
def assignments(request):
    """ Create assignments view """
    AssignmentFormSet = modelform_factory(Assignment, fields=("class_id","assignment_name","description"))
    if request.method == "POST":
        formset = AssignmentFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, f'Assignment Successfully Created')
            return redirect('profile')
    else:
        formset = AssignmentFormSet()

    return render(
        request, "gatorgrouper/assignments.html", {"title": "Create Assignments",'formset': formset}
    )


@login_required
def survey(request):
    """ Student's grouping preference? """
    return render(request, "gatorgrouper/survey.html", {"title": "Survey"})


@login_required
def groupResult(request):
    """ Group result view """
    return render(
        request, "gatorgrouper/viewing-groups.html", {"title": "Group Result"}
    )


@login_required
def add_students(request):
    """ Used to display current students in roster and provides option to add students """
    StudentFormSet = modelform_factory(Student, fields=("class_id", "first_name", "last_name"))
    if request.method == "POST":
        formset = StudentFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, f'Student Successfully Created')
            return redirect('add-students')
    else:
        formset = StudentFormSet()
    return render(
        request, "gatorgrouper/add-students.html", {"title": "Add a Student", "formset": formset}
    )


@login_required
def create_groups(request):
    """ Created groups using gatorgrouper functions """
    
    return render(
        request, "gatorgrouper/create-groups.html", {"title": "Create Groups"}
    )
