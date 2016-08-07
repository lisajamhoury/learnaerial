from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from listings.models import Listing 
from listings.models import Category
from listings.models import Offering
from listings.models import City 
from listings.models import State
from listings.models import MetroArea

def listings(request):
	listings = Listing.objects\
		.filter(published=True)\
		.order_by('name')

	metroareas = MetroArea.objects\
		.all()\
		.order_by('name')

	categories = Category.objects\
		.all()\
		.order_by('name')

	offerings = Offering.objects\
		.all()\
		.order_by('name')

	cities = City.objects\
		.all()\
		.order_by('name')

	context = {}
	context['listings'] = listings
	context['metroareas'] = metroareas
	context['categories'] = categories
	context['offerings'] = offerings
	context['cities'] = cities
	context['current_page'] = 'listings'

	return render(request, 'listings.html', context)


def listing(request, slug):
	try:
		listing = Listing.objects.get(slug=slug)
	except Listing.DoesNotExist: 
		return HttpResponseRedirect(reverse('listings'))
	template_name = 'listings-listing.html'

	context = {}
	context['listing'] = listing 
	context['current_page'] = 'listings_listing'

	if request.is_ajax():
		template_name = 'listing-modal.html'
		context['modal'] = True

	return render(request, template_name, context)

def listings_metro_area(request, slug):
	try:
		metro_area = MetroArea.objects.get(slug=slug)
	except MetroArea.DoesNotExist:
		return HttpResponseRedirect(reverse('listings'))
	template_name = 'listings-metro-area.html'

	listings = Listing.objects\
		.filter(published=True, city__metroarea=metro_area)\
		.order_by('name')

	categories = Category.objects\
		.all()\
		.order_by('name')

	offerings = Offering.objects\
		.all()\
		.order_by('name')

	cities = City.objects\
		.filter(metroarea=metro_area)\
		.order_by('name')

	context = {}
	context['metro_area'] = metro_area
	context['listings'] = listings
	context['categories'] = categories
	context['offerings'] = offerings
	context['cities'] = cities
	context['current_page'] = 'listings'

	return render(request, 'listings-metro-area.html', context)	


def listings_nyc(request):
	listings_nyc = Listing.objects\
		.filter(published=True, state__name__icontains="ny")\
		.order_by('name')

	categories = Category.objects\
		.all()\
		.order_by('name')

	offerings = Offering.objects\
		.all()\
		.order_by('name')

	cities = City.objects\
		.filter(state__name__icontains="ny")\
		.order_by('name')

	context = {}
	context['listings'] = listings_nyc
	context['categories'] = categories
	context['offerings'] = offerings
	context['cities'] = cities
	context['current_page'] = 'listings'

	return render(request, 'listings-nyc.html', context)

def listings_sf(request):
	listings_nyc = Listing.objects\
		.filter(published=True, state__name__icontains="ca")\
		.order_by('name')

	categories = Category.objects\
		.all()\
		.order_by('name')

	offerings = Offering.objects\
		.all()\
		.order_by('name')

	cities = City.objects\
		.filter(state__name__icontains="ca")\
		.order_by('name')

	context = {}
	context['listings'] = listings_nyc
	context['categories'] = categories
	context['offerings'] = offerings
	context['cities'] = cities
	context['current_page'] = 'listings'

	return render(request, 'listings-sf.html', context)