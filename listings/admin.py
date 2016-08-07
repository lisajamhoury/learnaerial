from django.contrib import admin

from listings.models import Listing 
from listings.models import City
from listings.models import State 
from listings.models import Country
from listings.models import Neighborhood
from listings.models import Category
from listings.models import Offering
from listings.models import	MetroArea

admin.site.register(Listing)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Neighborhood)
admin.site.register(Category)
admin.site.register(Offering)
admin.site.register(MetroArea)
