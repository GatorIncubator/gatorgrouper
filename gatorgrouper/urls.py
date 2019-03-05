""" This is undocumented """
# from django.urls import path,
from django.urls import path, re_path

# from django.conf import settings
# from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    path("group/", views.upload_csv, name="upload_csv"),
]
