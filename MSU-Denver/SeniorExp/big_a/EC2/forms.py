# forms.py
from django import forms

class SaveYAMLForm(forms.Form):
    destination_path = forms.CharField(label='Destination Path', max_length=1000)
    # Add other fields as needed, for example:
    # data = forms.CharField(widget=forms.Textarea, label='YAML Content')
