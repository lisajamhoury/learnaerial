from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.site.site_header = "Learn Aerial"
admin.autodiscover()

urlpatterns = [
    url(r'', include('main.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^listings/', include('listings.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
