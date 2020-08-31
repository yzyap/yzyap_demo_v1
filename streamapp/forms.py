from django import forms
from django.forms import Form

class CodeExecutorForm(Form):
    code = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":120}),label="Code")
    #code = forms.CharField(widget=forms.Textarea,label='Code')
