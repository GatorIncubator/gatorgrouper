""" This is undocumented """
from django.urls import path

# from django.urls import re_path

# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path(
        "", views.home, name="Gatorgrouper-home"
    ),  # first attribute is a space, meaning homepage
    path("classes", views.create_classes, name="Gatorgrouper-classes"),
    path("assignments", views.assignments, name="Gatorgrouper-assignments"),
    path("survey", views.survey, name="Gatorgrouper-survey"),
    path("group-result", views.groupResult, name="Gatorgrouper-groups"),
]
