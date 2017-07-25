from django.contrib import admin
from django import forms

from events.models import Event

class EventForm(forms.ModelForm):
	class Meta:
		model = Event 
		fields = '__all__'

	def clean(self):
		data = self.cleaned_data
		if not data.get('venue') and not data.get('venue_name'):
			raise forms.ValidationError('You must provide a venue or venue name')
		return self.cleaned_data

class EventAdmin(admin.ModelAdmin):
	form = EventForm
	exclude = ('slug',)

admin.site.register(Event, EventAdmin)
