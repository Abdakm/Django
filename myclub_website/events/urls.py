from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
	path("", views.home, name = "home"),
	path("<int:year>/<str:month>/", views.home, name = "home"),
	path("list_events/", views.list_events, name = "list_events"),
	path("add_venue", views.add_venue, name = "add_venue"),
	path("list_venues/", views.list_venues, name = "list_venues"),
	path("show_venue/<venue_id>", views.show_venue, name = "show_venue"),
	path("search_venue/", views.search_venue, name = "search_venue"),
	path("update_veneu/<venue_id>", views.update_venue, name = "update_venue"),
	path("delete_venue/<venue_id>/", views.delete_venue, name = "delete_venue"),
	path("add_event", views.add_event, name = "add_event"),
	path("update_event/<event_id>/", views.update_event, name = "update_event"),
	path("delete_event/<event_id>/", views.delete_event, name = "delete_event"),
	path('venue_text/', views.venue_text, name = "venue_text"),
	path('venue_csv/', views.venue_csv, name = "venue_csv"),
	path('my_events/', views.my_events, name = "my_events"),
	path('search_event/', views.search_event, name = "search_event"),
	path('admin_approval/', views.admin_approval, name = "admin_approval"),
	path('venue_events/<venue_id>/', views.venue_events, name = "venue_events"),
	path('show_event/<event_id>/', views.show_event, name = "show_event"),
]