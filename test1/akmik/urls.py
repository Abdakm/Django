from django.urls import path
from . import views


app_name = "akmik"
urlpatterns = [
	path("", views.home, name = "home"),
	path("akmik/<int:year>/<str:month>/", views.home, name = "home"),
	path("form/", views.form, name = "form"),
	path("information/", views.information, name = "information"),
]