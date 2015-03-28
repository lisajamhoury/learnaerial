from django.db import models
from django.core.urlresolvers import reverse 
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class Event(models.Model):
	published = models.BooleanField(default=False)
	ongoing = models.BooleanField(default=False)
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

	image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFit(300, 300, upscale=False)],
                                     format='JPEG',
                                     options={'quality': 85})

	image_feature = ImageSpecField(source='image',
                                     processors=[ResizeToFit(width=800, upscale=False)],
                                     format='JPEG',
                                     options={'quality': 85})




	def __unicode__(self):
		return u'%s' % self.name

	def get_absolute_url(self):
		return reverse('event-listing', args=[self.slug]) 
