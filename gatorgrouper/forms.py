""" Django forms to handle and validate user interaction with the website """
from django import forms


class UploadCSVForm(forms.Form):
    """ Form enabling the uploading of a CSV file to be used for grouping """

    student_data = forms.FileField(label="Student data CSV file")
    student_preferences = forms.FileField(label="Student preferences CSV file", required=False)
    numgrp = forms.TypedChoiceField(
        choices=[(str(2 ** i), str(2**i)) for i in range(1, 5)],  # Restrict choices to powers of 2
        coerce=int,
        label="Number of groups to create"
    )
