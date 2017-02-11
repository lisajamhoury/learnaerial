from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from events.feed import UpcomingEventsFeed

from main import views as main_views
from events import views as events_views 
from listings import views as listings_views


admin.site.site_header = "Learn Aerial"
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'learnaerial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', main_views.home, name='home'),
    url(r'^about$', main_views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^schools/new-york$', main_views.schools, name='schools'),
    url(r'^venues/new-york$', main_views.venues, name='venues'),
    url(r'^companies$', main_views.companies, name='companies'),
    url(r'^equipment$', main_views.equipment, name='equipment'),
    url(r'^newsletter_signup$', main_views.newsletter_signup, name='newsletter_signup'),
    url(r'^events$', events_views.events, name='events'),
    url(r'^events/archive$', events_views.events_archive, name='events-archive'),
    url(r'^events/feed$', UpcomingEventsFeed()),
    url(r'^events/(?P<slug>[\w\s,.%&-]+)$', events_views.event_listing, name='event-listing'),
    url(r'^listings$', listings_views.listings, name='listings'),
    url(r'^listings/metro/(?P<slug>[\w\s,.%&-]+)$', listings_views.listings_metro_area, name='listings_metro_area'), 
    url(r'^listings/(?P<slug>[\w\s,.%&-]+)$', listings_views.listing, name='listing'),
    url(r'^faq$', main_views.faq, name='faq')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
