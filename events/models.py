from django.db import models

class Event(models.Model):
	published = models.BooleanField(default=False)
	image = models.ImageField(null=True, blank=True, upload_to='events')
	name = models.CharField(max_length=500)
	slug = models.SlugField()
	venue = models.CharField(max_length=500)
	venue_url = models.CharField(max_length=500, null=True, blank=True)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)
	time = models.CharField(max_length=500, null=True, blank=True)
	price = models.CharField(max_length=500, null=True, blank=True)
	link = models.CharField(max_length=500, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return u'%s' % self.name
