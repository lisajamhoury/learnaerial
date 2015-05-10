import datetime

from django.db import models
from django.core.urlresolvers import reverse 
from django.utils.text import slugify
from django.conf import settings
from django.utils.timezone import get_default_timezone

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
	post_to_facebook = models.BooleanField(default=False)
	posted_to_facebook = models.BooleanField(default=False)
	post_to_facebook_after = models.DateTimeField(null=True, blank=True)

	image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFit(300, 300, upscale=False)],
                                     format='JPEG',
                                     options={'quality': 85})

	image_feature = ImageSpecField(source='image',
                                     processors=[ResizeToFit(width=1000, upscale=False)],
                                     format='JPEG',
                                     options={'quality': 100})

	def __unicode__(self):
		return u'%s' % self.name

	def get_absolute_url(self):
		return reverse('event-listing', args=[self.slug]) 

	def get_full_url(self):
		return settings.SITE_URL + self.get_absolute_url()

	def ready_to_post(self):
		now = datetime.datetime.now(get_default_timezone())

		if not self.post_to_facebook_after:
			return True

		if self.post_to_facebook_after <= now: 
			return True

	def save(self, *args, **kwargs):
		if self.slug == '' or self.slug is None:
			suffix = 0
			potential = base = slugify(self.name[:200])
			while True:
				if suffix != 0:
					potential = "-".join([base, str(suffix)])
				if Event.objects.filter(slug=potential).count() == 0:
					self.slug = potential
					break
				suffix += 1
		super(Event, self).save(*args, **kwargs)


