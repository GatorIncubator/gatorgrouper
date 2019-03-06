from django import forms

class UploadCSVForm(forms.Form):
    file = forms.FileField(label="Student data CSV file")
    numgrp = forms.IntegerField(min_value=2, max_value=25, label="Number of groups to create")
