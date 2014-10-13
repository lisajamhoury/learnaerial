import datetime

from django.shortcuts import render
from events.models import Event 


def events(request):
	now = datetime.datetime.now()
	events = Event.objects.filter(published=True).exclude(end_date__lte=now, start_date__lte=now).order_by('start_date')

	context = {}
	context['events'] = events
	context['current_page'] = 'events'

	return render(request, 'events.html', context)

def event_listing(request, slug):
	event = Event.objects.get(slug=slug)

	context = {}
	context['event'] = event 
	context['current_page'] = 'event_listing'

	return render(request, 'event-listing.html', context)
