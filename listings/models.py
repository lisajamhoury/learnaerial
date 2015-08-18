from urlparse import urlparse

from django.db import models
from django.core.urlresolvers import reverse 

from django_extensions.db.fields import AutoSlugField


class City(models.Model):
	name = models.CharField(max_length=200)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
	class Meta:
		verbose_name_plural = "Cities"

	def __unicode__(self):
		return self.name


class State(models.Model):
	name = models.CharField(max_length=200)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')

	def __unicode__(self):
		return self.name


class Country(models.Model):
	name = models.CharField(max_length=200)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
	class Meta:
		verbose_name_plural = "Countries"

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
	name= models.CharField(max_length=500)
	slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
	image = models.ImageField(null=True, blank=True, upload_to='listings')
	website = models.CharField(max_length=500, null=True, blank=True)
	neighborhood = models.ForeignKey(Neighborhood, null=True)
	address_1 = models.CharField(max_length=500, null=True, blank=True)
	address_2 = models.CharField(max_length=500, null=True, blank=True)
	city = models.ForeignKey(City, null=True)
	state = models.ForeignKey(State, null=True)
	zipcode = models.CharField(max_length=15, null=True, blank=True)
	country = models.ForeignKey(Country, null=True)
	description = models.TextField(null=True, blank=True)
	categories = models.ManyToManyField(Category)
	offerings = models.ManyToManyField(Offering, null=True)

	def __unicode__(self):
		return self.name

	def short_website(self):
		parts = urlparse(self.website)
		return parts.netloc
	
	# def get_absolute_url(self):
	# 	return reverse('listings-listing', args=[self.slug]) 
