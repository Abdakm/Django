from django.contrib import admin
from .models import Std_Info

class Std_Info_view(admin.ModelAdmin):
    list_display = ("firstname", "lastname")
    ordering = ("id",)

admin.site.register(Std_Info, Std_Info_view)