from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from events.feed import UpcomingEventsFeed

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learnaerial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^about$', 'main.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^schools/new-york$', 'main.views.schools', name='schools'),
    url(r'^venues/new-york$', 'main.views.venues', name='venues'),
    url(r'^companies$', 'main.views.companies', name='companies'),
    url(r'^equipment$', 'main.views.equipment', name='equipment'),
    url(r'^newsletter_signup$', 'main.views.newsletter_signup', name='newsletter_signup'),
    url(r'^events$', 'events.views.events', name='events'),
    url(r'^events/archive$', 'events.views.events_archive', name='events-archive'),
    url(r'^events/feed$', UpcomingEventsFeed()),
    url(r'^events/(?P<slug>[\w\s,.%&-]+)$', 'events.views.event_listing', name='event-listing'),
    url(r'^listings$', 'listings.views.listings', name='listings'),
    url(r'^listings/newyorkcity$', 'listings.views.listings_nyc', name='listings-nyc'),
    url(r'^listings/sanfrancisco$', 'listings.views.listings_sf', name='listings-sf'),
    url(r'^listings/(?P<slug>[\w\s,.%&-]+)$', 'listings.views.listing', name='listing'),
    url(r'^faq$', 'main.views.faq', name='faq')
    # url(r'^places$', 'listings.views.listings', name='places'),
    # url(r'^places/(?P<slug>[\w\s,.%&-]+)$', 'listings.views.listing', name='place')


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
