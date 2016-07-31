import mailchimp
import json

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from main.forms import NewsletterForm


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

def newsletter_signup(request):
	error_message = 'Sorry! Something went wrong. Please try again.'

	if request.method == 'POST':
		form = NewsletterForm(request.POST)
		
		if form.is_valid():
			email = {'email': form.cleaned_data['email']}
			first_name = form.cleaned_data['fname']
			last_name = form.cleaned_data['lname']
			
			merge_vars = {'FNAME': first_name, 'LNAME': last_name}
			mc = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
			
			try:
				response = mc.lists.subscribe(id='6e0c3fe71f', double_optin=False, email=email, merge_vars=merge_vars)
				success = {'success': True}
				return HttpResponse(json.dumps(success), content_type='application/json')
			
			except mailchimp.Error as e:
				error_message = e.message

		else: 
			if 'email' in form.errors:
				error_message = form.errors['email'][0]

		response = {'success': False, 'error_message': error_message}

		return HttpResponse(json.dumps(response), content_type='application/json')

def faq(request):
	context = {}
	context['current_page'] = 'faq'

	return render(request, 'faq.html', context)




