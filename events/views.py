import datetime

from django.shortcuts import render
from django.db.models import Q
from events.models import Event


def events(request):
	now = datetime.datetime.now()
	# events = Event.objects.filter(ongoing=False, published=True).exclude(end_date__lt=now, start_date__lte=now).order_by('start_date')
	events = Event.objects\
		.filter(ongoing=False, published=True)\
		.exclude(Q(end_date__lt=now) | Q(end_date__isnull=True), start_date__lt=now)\
		.order_by('start_date')

	ongoing_events = Event.objects.filter(ongoing=True, published=True)

	context = {}
	context['events'] = events
	context['current_page'] = 'events'
	context['ongoing_events'] = ongoing_events


	return render(request, 'events.html', context)

def event_listing(request, slug):
	event = Event.objects.get(slug=slug)

	context = {}
	context['event'] = event
	context['current_page'] = 'event_listing'

	return render(request, 'event-listing.html', context)

def events_archive(request):
	now = datetime.datetime.now()
	events_archive = Event.objects.filter(Q(end_date__lt=now) | Q(end_date__isnull=True), start_date__lt=now, ongoing=False).order_by('-start_date')

	context = {}
	context['current_page'] = 'events'
	context['events_archive'] = events_archive

	return render(request, 'events-archive.html', context)

