from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.listings, name='listings'),
    url(r'^submit/?$', views.listing_submit, name='listing_submit'), 
    url(r'^thanks/?$', views.listings_thanks, name='listings_thanks'), 
    url(r'^metro/(?P<slug>[\w\s,.%&-]+)$',
        views.listings_metro_area, name='listings_metro_area'),
    url(r'^(?P<slug>[\w\s,.%&-]+)$', views.listing, name='listing'),
]
