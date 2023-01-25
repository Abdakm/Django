from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm >> in forms.py pageN
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm

def login_user(request):
	if request.method == "POST":
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        return redirect('events:home')
	    else:
	    	message = "There was an Error  Logging In, Try Again..."
	    	messages.success(request, (message))
	    	return redirect('login')
	else:
		return render(request, 'authenticate/login.html')

def logout_user(request):
	logout(request)
	message = "You Were Logged Out!"
	messages.success(request, (message))
	return redirect('events:home')

def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, ("Registeration Success"))
			return redirect('events:home')
	else:
		form = RegisterUserForm()

	return render(request, 'authenticate/register_user.html', {
			'form' : form
		})