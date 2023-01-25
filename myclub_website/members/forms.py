from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	# password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", 'email', 'password1', 'password2')

		# def __int__(self, *args, **kwargs):
		# 	super(RegisterUserForm, self).__int__(*args, **kwargs)

		# 	self.fields['username'].widget.attrs.update['class'] ='form-control'
		# 	self.fields['password1'].widget.attrs['class'] ='form-control'
		# 	self.fields['password2'].widget.attrs['class'] = 'form-control'
		# 	self.fields['password1'].label = "hello"

		widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control', 'id':'test'}),
			'password1' : forms.PasswordInput(attrs={'class':'form-control'})
		}