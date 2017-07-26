from django.contrib import admin
from django.forms import ModelForm
from django import forms

from listings.models import Listing 
from listings.models import City
from listings.models import State 
from listings.models import Country
from listings.models import Neighborhood
from listings.models import Category
from listings.models import Offering
from listings.models import MetroArea


class ListingAdminForm(ModelForm):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        help_text='This is used on the listings section of the website.'
    )
    freeform_city = forms.CharField(
        required=False,
        help_text='This is for user input from website form. Use city field instead. Do not enter here.'
    )
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        help_text='This is used on the listings section of the website.'
    )
    freeform_country = forms.CharField(
        required=False,
        help_text='This is for user input from website form. Use country field instead. Do not enter here.'
    )
    contact_email = forms.CharField(
        required=False,
        help_text='This is for user input from website form. Should not be made public. Do not enter here.'
    )

    class Meta:
        model = Listing
        fields = '__all__'


class ListingAdmin(admin.ModelAdmin):
    form = ListingAdminForm

admin.site.register(Listing, ListingAdmin)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Neighborhood)
admin.site.register(Category)
admin.site.register(Offering)
admin.site.register(MetroArea)
