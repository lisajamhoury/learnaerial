from django import forms

from listings.models import Listing

class ListingForm(forms.ModelForm):
	name = forms.CharField(required=True, label='Listing Name')
	freeform_city = forms.CharField(required=True, label='City')
	freeform_country = forms.CharField(required=True, label='Country')
	contact_email = forms.CharField(required=False, label='Contact Email Address', help_text="Optionally enter a contact email. This will not be displayed publicly.")
	description = forms.CharField(required=False, widget=forms.Textarea, help_text='Optionally write a short description about this listing.')

	class Meta: 
		model = Listing
		fields = ('name', 'website', 'address_1', 'address_2', 'freeform_city', 'state', 'zipcode', 'freeform_country', 'categories', 'offerings', 'description', 'contact_email')
