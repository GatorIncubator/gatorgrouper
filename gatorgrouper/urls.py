""" This is undocumented """
<<<<<<< HEAD
from django.urls import path

# from django.urls import re_path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.home, name="Gatorgrouper-home"),
    path("classes/", views.create_classes, name="Gatorgrouper-classes"),
    path("assignments/", views.assignments, name="Gatorgrouper-assignments"),
    path("survey/", views.survey, name="Gatorgrouper-survey"),
    path("group-result/", views.groupResult, name="Gatorgrouper-groups"),
=======
from django.conf.urls import url
from . import views

urlpatterns = [
    url("group", views.upload_csv, name="upload_csv"),
    url("classes", views.create_classes, name="Gatorgrouper-classes"),
    url("assignments", views.assignments, name="Gatorgrouper-assignments"),
    url("survey", views.survey, name="Gatorgrouper-survey"),
    url("group-result", views.groupResult, name="Gatorgrouper-groups"),
    url(
        "", views.home, name="Gatorgrouper-home"
    ),  # first attribute is a space, meaning homepage
>>>>>>> master
]
