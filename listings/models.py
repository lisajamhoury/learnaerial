from urlparse import urlparse

from django.db import models
from django.core.urlresolvers import reverse 

from django_extensions.db.fields import AutoSlugField


class State(models.Model):
	name = models.CharField(max_length=200)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')

	class Meta:
		ordering = ('name', )

	def __unicode__(self):
		return self.name

class Country(models.Model):
	name = models.CharField(max_length=200)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
	class Meta:
		verbose_name_plural = "Countries"

	def __unicode__(self):
		return self.name

class MetroArea(models.Model): 
	name = models.CharField(max_length=200)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
	state = models.ForeignKey(State)
	class Meta:
		verbose_name_plural = "MetroAreas"

	def __unicode__(self):
		return self.name 

class City(models.Model):
	name = models.CharField(max_length=200)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
	state = models.ForeignKey(State, null=True)
	metroarea = models.ForeignKey(MetroArea, null=True)
	
	class Meta:
		verbose_name_plural = "Cities"

	def __unicode__(self):
		return self.name


class Neighborhood(models.Model):
	name = models.CharField(max_length=200)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
	city = models.ForeignKey(City)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
		
	class Meta:
		verbose_name_plural = "Categories"
		ordering = ['name']

	def __unicode__(self):
		return self.name


class Offering(models.Model):
	name = models.CharField(max_length=200)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')

	def __unicode__(self):
		return self.name
	

class Listing(models.Model): 
	published = models.BooleanField(default=False)
	name = models.CharField(max_length=500)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
	image = models.ImageField(null=True, blank=True, upload_to='listings')
	website = models.CharField(max_length=500, null=True, blank=True)
	neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True)
	address_1 = models.CharField(max_length=500, null=True, blank=True)
	address_2 = models.CharField(max_length=500, null=True, blank=True)
	city = models.ForeignKey(City, null=True, blank=True, help_text='Enter city here. This is used on the listings section of the website.')
	freeform_city = models.CharField(max_length=500, null=True, blank=True, help_text=' Do not enter here. This is for user input from website form. Use city field instead.')
	state = models.ForeignKey(State, null=True, blank=True)
	zipcode = models.CharField(max_length=15, null=True, blank=True)
	country = models.ForeignKey(Country, null=True, help_text='Enter country here. This is used on the listings section of the website.')
	freeform_country = models.CharField(max_length=500, null=True, blank=True, help_text='Do not enter here. This is for user input from website form. Use country field instead.')
	description = models.TextField(null=True, blank=True)
	categories = models.ManyToManyField(Category)
	offerings = models.ManyToManyField(Offering)
	contact_email = models.CharField(max_length=500, null=True, blank=True, help_text='Do not enter here. This is for user input from website form. Should not be made public.')

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name

	def short_website(self):
		parts = urlparse(self.website)
		return parts.netloc
	
	def get_absolute_url(self):
		return reverse('listing', args=[self.slug])