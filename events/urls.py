from django.conf.urls import url

from .feed import UpcomingEventsFeed
from . import views

urlpatterns = [
    url(r'^$', views.events, name='events'),
    url(r'^archive$', views.events_archive, name='events-archive'),
    url(r'^feed$', UpcomingEventsFeed()),
    url(r'^(?P<slug>[\w\s,.%&-]+)$', views.event_listing, name='event-listing'),
]
