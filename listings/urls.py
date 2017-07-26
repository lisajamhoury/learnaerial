from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listings, name='listings'),
    url(r'^add/?$', views.listing_add, name='listing_add'), 
    url(r'^metro/(?P<slug>[\w\s,.%&-]+)$',
        views.listings_metro_area, name='listings_metro_area'),
    url(r'^(?P<slug>[\w\s,.%&-]+)$', views.listing, name='listing'),
]
