from django.shortcuts import render
from events.models import Event 

def events(request):
	events = Event.objects.filter(published=True).order_by('-start_date')

	context = {}
	context['events'] = events

	return render(request, 'events.html', context)

def event_listing(request, slug):
	event = Event.objects.get(slug=slug)

	context = {}
	context['event'] = event 

	return render(request, 'event-listing.html', context)
