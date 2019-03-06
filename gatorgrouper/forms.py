from django import forms

class UploadCSVForm(forms.Form):
    file = forms.FileField() # CSV file to be uploaded & parsed
    numgrp = forms.IntegerField(min_value=2, max_value=25) # Number of groups to create
