""" This is undocumented """
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path(
        "", views.home, name="Gatorgrouper-home"
    ),  # first attribute is a space, meaning homepage
    path("group/", views.upload_csv, name="upload_csv"),
    path("classes", views.create_classes, name="Gatorgrouper-classes"),
    path("assignments", views.assignments, name="Gatorgrouper-assignments"),
    path("survey", views.survey, name="Gatorgrouper-survey"),
    path("group-result", views.groupResult, name="Gatorgrouper-groups"),
]
