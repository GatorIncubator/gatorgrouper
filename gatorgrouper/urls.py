""" This is undocumented """
from django.urls import path
from . import views
from .views import AssignmentView

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("", views.home, name="Gatorgrouper-home"),
    path("classes/", views.create_classes, name="Gatorgrouper-classes"),
    path("assignments/", views.assignments, name="Gatorgrouper-assignments"),
    path("survey/", views.survey, name="Gatorgrouper-survey"),
    path("add-students/", views.add_students, name="add-students"),
    path("create-groups/", views.create_groups, name="create-groups"),
    path("upload-csv/", views.upload_csv, name="upload-csv"),
    path("assignment/<int:pk>/", AssignmentView.as_view(), name="assignment-detail"),
]
