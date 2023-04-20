from django import forms
from app.models import *
class StudentForm(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField(max_length=100)
    semail=forms.EmailField()
    