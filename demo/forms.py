from django import forms
import os


class FileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'file-input'
    }))


class SelectedHeadersForm(forms.Form):
    json = forms.CharField(widget=forms.HiddenInput(attrs={
        'id': 'headerSelector'
    }))
