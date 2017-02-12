from __future__ import unicode_literals
from urllib import urlencode
from autoslug import AutoSlugField


from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    slug = AutoSlugField(populate_from='title')
    order = models.IntegerField(default=0)
    page_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    body = models.TextField(blank=True, verbose_name="Post Content")
    summary = models.TextField(blank=True, verbose_name="Post Summary")
    author = models.ForeignKey('blog.Author', null=True, blank=True)
    related_posts = models.ManyToManyField('blog.Post', blank=True)
    categories = models.ManyToManyField('blog.Category', blank=True)
    listings = models.ManyToManyField('listings.Listing', blank=True)
    published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(blank=True, null=True)

    thumbnail_image = models.ImageField(null=True, blank=True, upload_to='blog/thumbnails')
    banner_image = models.ImageField(null=True, blank=True, upload_to='blog/banner')

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-publish_date', '-created']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])

    def get_share_url(self):
        return settings.SITE_URL + self.get_absolute_url()

    def get_social_promotion(self):
        social_promotion = self.title
        return social_promotion

    def twitter_share_url(self):
        status = '%s %s' % (self.get_social_promotion(), self.get_share_url())

        params = {
            'status': status
        }

        base_url = 'https://twitter.com/home?'

        return base_url + urlencode(params, 'utf-8')

    def facebook_share_url(self):
        params = {
            'u': self.get_share_url()
        }

        base_url = 'https://www.facebook.com/sharer/sharer.php?'

        return base_url + urlencode(params, 'utf-8')


class Author(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_category', args=[self.slug])

    class Meta:
        verbose_name_plural = 'Categories'
