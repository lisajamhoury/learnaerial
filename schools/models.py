from django.db import models


class Neighborhood(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField()


class City(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField()


class State(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField()


class Country(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField()


class School(models.Model):
	name = models.CharField(max_length=500)
	slug = models.SlugField()
	image = models.ImageField(null=True, blank=True, upload_to='schools')
	website = models.CharField(max_length=500, null=True, blank=True)
	neighborhood = models.ForeignKey(Neighborhood, null=True)
	address_1 = models.CharField(max_length=500, null=True, blank=True)
	address_2 = models.CharField(max_length=500, null=True, blank=True)
	city = models.ForeignKey(City, null=True)
	state = models.ForeignKey(State, null=True)
	country = models.ForeignKey(Country, null=True)
	description = models.TextField(null=True, blank=True)
