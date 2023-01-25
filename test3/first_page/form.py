from django import forms
from django.forms import ModelForm
from .models import Std_Info

class Std_Info_Form(ModelForm):
    class Meta:
        model = Std_Info
        fields = ("__all__")
        labels = {
            "firstname" : "",
            "lastname" : ""
        }
        widgets = {
            "firstname" : forms.TextInput(attrs = {'class':'form-control','placeholder':'First Name'}),
            "lastname" : forms.TextInput(attrs = {'class':'form-control','placeholder':'Last Name'})
        }