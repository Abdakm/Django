from django.shortcuts import render
from .form import InformationFrom, SubjectsForm, StdSubjectsForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Information
# Create your views here.
def index(request):
	form = InformationFrom
	if request.method == 'POST':
		form = InformationFrom(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('information', args=("info", )))

	return render(request, 'pages/form_page.html',{
		'form' : form
		})

def information(request):
		info = Information.objects.all()
		return render(request, "pages/information.html",{
			"info" : info,
			})

def show_information(request, information_id):
	person = Information.objects.get(pk=information_id)
	return render(request, "pages/show_information.html", {
		"person" : person,
		})

def searched(request):
	if request.method == "POST":
		searched = request.POST.get("searched")
		names = Information.objects.filter(firstname__contains=searched)
		return render(request,"pages/searched.html",{
			"searched" : searched,
			"names" : names,
			})
	else:
		return render(request,"pages/searched.html",{
			"searched" : searched,
			"names" : names,
			})
