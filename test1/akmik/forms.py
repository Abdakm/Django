from .models import Information
from django import forms
from django.forms import ModelForm

class InformationForm(ModelForm):
	class Meta:
		model = Information
		fields = (
		"First_Name",
		"Last_Name",
		"Email",
		"Password",
		"Re_Password"
			)
		labels = {
		"First_Name":"",
		"Last_Name":"",
		"Email":"",
		"Password":"",
		"Re_Password":""
		}
		widgets = {
		"First_Name": forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Your First_Name'}),
		"Last_Name": forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Your Last_Name'}),
		"Email":forms.EmailInput(attrs = {'class':'form-control','placeholder':'Enter Your Email'}),
		"Password":forms.PasswordInput(attrs = {'class':'form-control','placeholder':'Enter Your Password'}),
		"Re_Password":forms.PasswordInput(attrs = {'class':'form-control','placeholder':'Enter Your Re_Password'})
		}