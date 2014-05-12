from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
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
    url(r'^events$', 'events.views.events', name='events'),
    url(r'^events/(?P<slug>[\w\s,.%&-]+)$', 'events.views.event_listing', name='event-listing'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
