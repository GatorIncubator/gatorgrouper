from django import forms

class UploadCSVForm(forms.Form):
    file = forms.FileField()
