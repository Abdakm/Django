from django.urls import path
from . import views

urlpatterns = [
    path('', views.std_form, name = "std_form"),
    path('search/', views.search, name = "search"),
    path('information/', views.information, name = "information"),
    path('show_user/<user_id>/', views.show_user, name = "show_user"),
    path('update/<user_id>/', views.update, name = "update"),
]