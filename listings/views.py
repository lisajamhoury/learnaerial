from django.shortcuts import render
from listings.models import Listing 
from listings.models import Category
from listings.models import Offering
from listings.models import City 

def listings(request):
	listings = Listing.objects\
		.filter(published=True)\
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
	context['categories'] = categories
	context['offerings'] = offerings
	context['cities'] = cities

	return render(request, 'listings.html', context)


def listing(request, slug):
	listing = Listing.objects.get(slug=slug)
	template_name = 'listings-listing.html'

	context = {}
	context['listing'] = listing 

	if request.is_ajax():
		template_name = 'listing-modal.html'
		context['modal'] = True

	return render(request, template_name, context)	
