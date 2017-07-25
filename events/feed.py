import datetime

from django.db.models import Q
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.conf import settings
from django.template.defaultfilters import truncatewords

from events.models import Event


class UpcomingEventsFeed(Feed):
    title = "Learn Aerial Upcoming Events NYC"
    link = "/events/feed"
    description = "Upcoming aerial events in New York City"

    def items(self):
        today = datetime.date.today()
        sixdays = today + datetime.timedelta(days=6)
        return Event.objects.filter(
            Q(start_date__gte=today, start_date__lte=sixdays) | Q(start_date__lt=today, end_date__gt=today),
            ongoing=False, 
            published=True).order_by('start_date')


    def item_title(self, item):
        return item.name

    def item_author_name(self, item):
        return item.get_venue_name() 

    def item_enclosure_url(self, item):
        return item.get_venue_url(absolute=True)

    def item_description(self, item):
        truncated_description = truncatewords(item.description, 50)
        return truncated_description

    def item_pubdate(self, item):
        return datetime.datetime.combine(item.start_date, datetime.time())

