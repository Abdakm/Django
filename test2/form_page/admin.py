from django.contrib import admin
from .models import Information, StdSubjects, Subjects

# Register your models here.

class Informationview(admin.ModelAdmin):
	list_display = ('id','firstname', 'lastname', 'email', 'password')
	ordering = ("id",)
	list_filter = ('firstname', 'lastname')
	fields = (('firstname', 'lastname'), 'email', ('password', 'repassword'))

admin.site.register(Information, Informationview)
admin.site.register(StdSubjects)
admin.site.register(Subjects)