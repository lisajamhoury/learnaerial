from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def schools(request):
	return render(request, 'schools.html')

def venues(request):
	return render(request, 'venues.html')

def companies(request):
	return render(request, 'companies.html')

def equipment(request):
	return render(request, 'equipment.html')

