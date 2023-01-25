from django.contrib import admin
from .models import Information
# Register your models here.

class InformationView(admin.ModelAdmin):
	list_display = ('First_Name', 'Last_Name', 'Email', 'Password')

admin.site.register(Information, InformationView)