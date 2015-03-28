from django.contrib import admin

from schools.models import School, Neighborhood, City, State, Country 

admin.site.register(School)
admin.site.register(Neighborhood)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)

# Register your models here.
