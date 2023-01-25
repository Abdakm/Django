from django.shortcuts import render
from datetime import datetime
from .forms import InformationForm
from django.http import HttpResponseRedirect
from .models import Information

# Create your views here.
def home(request, year = datetime.now().year, month = datetime.now().strftime("%B")):
	name = "akmik"
	age = 23
	now = datetime.now()
	year = now.year
	month = now.month
	return render(request, "events/home.html",{
		"name" : name,
		"age" : age,
		"year" : year,
		"month" : month
		})

def form(request):
	submitted = False
	if request.method == "POST":
		form = InformationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/form?submitted=True')
	else:
		form = InformationForm
		if "submitted" in request.GET:
			submitted = True

	return render(request, "events/forms.html",{
		"form" : form,
		"submitted" : submitted
		})

def information(request):
	info = Information.objects.all()
	count = 0
	return render(request,'events/information.html',{
		"information" : info,
		"count" : count
		})