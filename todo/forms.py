from django import forms
from django.forms import fields
from .models import list1

class listForm(forms.ModelForm):
    class Meta:
        model= list1
        fields= ["date","item","completed"]