from django.contrib import admin

from events.models import Event

class EventAdmin(admin.ModelAdmin):
	exclude = ('slug',)

admin.site.register(Event, EventAdmin)
