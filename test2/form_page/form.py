from django import forms
from django.forms import ModelForm
from .models import Information, Subjects, StdSubjects

class InformationFrom(ModelForm):
	class Meta:
		model = Information
		fields = ("__all__")
		labels = {
		'firstname':'',
		'lastname':'',
		'email':'',
		'password':'',
		'repassword':''
		}
		widgets = {
		'firstname':forms.TextInput(attrs = {'class':'form-control','placeholder':'firstname'}),
		'lastname':forms.TextInput(attrs = {'class':'form-control','placeholder':'lastname'}),
		'email':forms.EmailInput(attrs = {'class':'form-control','placeholder':'email'}),
		'password':forms.PasswordInput(attrs = {'class':'form-control','placeholder':'password'}),
		'repassword':forms.PasswordInput(attrs = {'class':'form-control','placeholder':'repassword'})
		}

class SubjectsForm(ModelForm):
	class Meta:
		model = Subjects
		fields = ("__all__")
		labels = {
		"subject_name":'',
		'subject_number':''
		}
		widgets = {
		'subject_name':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Subject Name'}),
		'subject_number':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Subject Number'}),
		}

class StdSubjectsForm(ModelForm):
	class Meta:
		model = StdSubjects
		fields = ("__all__")
		labels = {
		'std_name':'',
		'subjects':''
		}
		widgets = {
		'std_name':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Std Name'}),
		'subjects':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Subjects'}),
		}

