from django.urls import path
from . import views

# app_name = "akmik"
urlpatterns = [
	path("", views.index, name = 'index'),
	path('information/', views.information, name = 'information'),
	path('show_information/', views.show_information, name = 'show_information'),
	path('searched/', views.searched, name = 'searched'),
]