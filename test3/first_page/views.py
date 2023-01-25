from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import Std_Info_Form
from .models import Std_Info

# Create your views here.
def std_form(request):
    if request.method == "POST":
        form = Std_Info_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('information'))
    else:
        form = Std_Info_Form
        return render(request, "pages/form_std.html", {
            "form" : form
        })
    
def information(request):
    info = Std_Info.objects.all()
    return render(request, "pages/information.html", {
        "info" : info
    })

def search(request):
    if request.method == "POST":
        search = request.POST.get("search") # catch input value
        user = Std_Info.objects.filter(firstname__contains=search)
        return render(request, "pages/search.html", {
            "search" : search,
            "users" : user,
        })
    else:
        return render(request, "pages/search.html")
    
def show_user(request, user_id):
    user = Std_Info.objects.get(pk=user_id)
    return render(request, "pages/show_user.html", {
        "user" : user
    })
def update(request, user_id):
    user = Std_Info.objects.get(pk=user_id)
    cont = Std_Info_Form(request.POST or None, instance=user)
    if cont.is_valid():
        cont.save()
        return redirect("/information/")
    return render(request, "pages/update.html", {
        "user" : user,
        "cont" : cont,
    })