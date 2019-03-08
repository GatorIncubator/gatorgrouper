""" Django forms to handle and validate user interaction with the website """
from django import forms


class UploadCSVForm(forms.Form):
    """ Form enabling the uploading of a CSV file to be used for grouping """

    file = forms.FileField(label="Student data CSV file")
    numgrp = forms.IntegerField(
        min_value=2, max_value=25, label="Number of groups to create"
    )

class StudentCompatibilityForm(forms.Form):
    """ Survey question allowing students to rate their compatibility with potential teammates"""
    preferred = forms.BooleanField()

StudentCompatibilityFormSet = forms.formset_factory(StudentCompatibilityForm)
