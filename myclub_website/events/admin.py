from django.contrib import admin
from .models import Venue, MyClubUser, Event


# @admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone')
	ordering = ('-name',)
	search_fields = ('name', 'address')

#OR Delete @admin.... and set this row below

admin.site.register(Venue, VenueAdmin)
admin.site.register(MyClubUser)

class EventAdmin(admin.ModelAdmin):
	fields = (('name', 'venue'), 'event_date', 'manager', 'description')
	list_display = ('name', 'event_date', 'venue')
	list_filter = ('event_date', 'venue')
	ordering = ('-event_date',)


admin.site.register(Event, EventAdmin)