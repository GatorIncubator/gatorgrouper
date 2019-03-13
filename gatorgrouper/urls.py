""" This is undocumented """
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url("group/", views.upload_csv, name="upload_csv"),
    url("classes", views.create_classes, name="Gatorgrouper-classes"),
    url("assignments", views.assignments, name="Gatorgrouper-assignments"),
    path("class/<int:class_id>/survey", views.survey, name="Gatorgrouper-survey"),
    url("group-result", views.groupResult, name="Gatorgrouper-groups"),
    url(
        "", views.home, name="Gatorgrouper-home"
    ),  # first attribute is a space, meaning homepage
]
