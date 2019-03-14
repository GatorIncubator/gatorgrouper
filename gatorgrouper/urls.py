""" This is undocumented """
from django.urls import path

# from django.urls import re_path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("", views.home, name="Gatorgrouper-home"),
    path("classes/", views.create_classes, name="Gatorgrouper-classes"),
    path("assignments/", views.assignments, name="Gatorgrouper-assignments"),
    path("survey/", views.survey, name="Gatorgrouper-survey"),
    path("group-result/", views.groupResult, name="Gatorgrouper-groups"),
    path("add-students/", views.add_students, name="add-students"),
    path("create-groups/", views.create_groups, name="create-groups"),
]
