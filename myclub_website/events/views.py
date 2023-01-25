from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm, EventFormAdmin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import csv
from django.contrib.auth.models import User
from django.core.paginator import Paginator #(next-page) (preves-page)
from django.contrib import messages

# Create your views here.

def home(request, year = datetime.now().year, month = datetime.now().strftime('%B')):
	name = "Akmik"
	month = month.title() # or month.capitalize()
	# Convert month from name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# create a calendar
	cal = HTMLCalendar().formatmonth(
			year,
			month_number
		)
	# Get current year
	now = datetime.now()
	current_year = now.year

	#Get current time
	time = now.strftime("%I:%M:%S %p")

	event_list = Event.objects.filter(
			event_date__year = 2022,
			event_date__month = 10
		)
	return render(request, "events/home.html", {
		"name" : name,
		"year" : year,
		"month" : month,
		"month_number" : month_number,
		"cal" : cal,
		"current_year" : current_year,
		"time" : time,
		"event_list" : event_list
		})

def show_venue(request, venue_id): # click on link venue
	venue = Venue.objects.get(pk=venue_id)
	venue_owner = User.objects.get(pk=venue.owner)
	return render(request, "events/show_venue.html",{
		"venue" : venue,
		"venue_owner" : venue_owner
		})

def search_venue(request): # click search
	if request.method == "POST":
		searched = request.POST.get("searched")
		venues = Venue.objects.filter(name__contains=searched)
		return render(request, "events/search_venue.html", {
			"searched" : searched,
			"venues" : venues
			})
	else:
		return render(request, "events/search_venue.html", {

			})


def add_venue(request):
	submitted = False
	if request.method == "POST":
		form = VenueForm(request.POST, request.FILES) #get the information add pass it to VenueFrom
		if form.is_valid():
			venue = form.save(commit=False)
			venue.owner = request.user.id
			venue.save()
			# form.save()
			return HttpResponseRedirect('/add_venue?submitted=True')
	else:
		form = VenueForm
		if "submitted" in request.GET:
			submitted = True

	return render(request, 'events/add_venue.html',{
			"form" : form,
			"submitted" : submitted
		})

def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, request.FILES or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('/list_venues/')#from urls.py
	return render(request, "events/update_venue.html",{
		"venue" : venue,
		"form" : form,
		})

def list_venues(request):
	#set up pagination
	p = Paginator(Venue.objects.all(), 2)
	page = request.GET.get('page')
	venues = p.get_page(page)
	nums = 'a' * venues.paginator.num_pages

	return render(request, "events/venue.html",{
		'venues' : venues,
		'nums' : nums
		})

def delete_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue.delete()
	return redirect('/list_venues/')


def add_event(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = EventFormAdmin(request.POST) #get the information add pass it to VenueFrom
		else:
			form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_event?submitted=True')
	else:
		# Just Going To The Page, Not Submitting
		if request.user.is_superuser:
			form = EventFormAdmin
		else:
			form = EventForm
		if "submitted" in request.GET:
			submitted = True

	return render(request, 'events/add_event.html',{
			"form" : form,
			"submitted" : submitted
		})

def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('/list_events/')# name from urls.py
	return render(request, "events/update_event.html",{
		"event" : event,
		"form" : form,
		})

def list_events(request):
	event_list = Event.objects.all().order_by('?')
	return render(request, "events/events_list.html", {
		"event_list" : event_list
		})

def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.user == event.manager:
		event.delete()
	else:
		messages.success(request, ("You don't have permition"))

	return redirect('/list_events/')

def venue_text(request):
	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=venues.txt'
	venues = Venue.objects.all()

	lines = ['Hello	']
	for venue in venues:
		lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n')

	response.writelines(lines)
	return response

def venue_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=venues.csv'

	# create a csv writer
	writer = csv.writer(response)

	# Add column headings to the csv file
	writer.writerow(['Venue Name', 'Address', 'Zip_Code', 'Phone', 'Web', 'Email_Address'])

	venues = Venue.objects.all()

	for venue in venues:
		writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address])

	return response

def my_events(request):
	if request.user.is_authenticated:
		me = request.user.id
		events = Event.objects.filter(attendees=me)
		return render(request, "events/my_events.html", {
			"events" : events
			})

	else:
		messages.success(request, ("Your don't logied in!!!"))
		return redirect('events:home')

def search_event(request):
	searched = request.POST.get("searched")
	events = Event.objects.filter(name__contains=searched)
	return render(request, "events/search_event.html", {
		'searched' : searched,
		'events' : events
		})