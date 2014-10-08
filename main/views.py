from django.shortcuts import render

# Create your views here.
def home(request):

	context = {}
	context['current_page'] = 'home'

	return render(request, 'home.html', context)

def about(request):

	context = {}
	context['current_page'] = 'about'

	return render(request, 'about.html', context)

def schools(request):

	context = {}
	context['current_page'] = 'schools'

	return render(request, 'schools.html', context)

def venues(request):

	context = {}
	context['current_page'] = 'venues'

	return render(request, 'venues.html', context)

def companies(request):

	context = {}
	context['current_page'] = 'companies'

	return render(request, 'companies.html', context)

def equipment(request):

	context = {}
	context['current_page'] = 'equipment'

	return render(request, 'equipment.html', context)

