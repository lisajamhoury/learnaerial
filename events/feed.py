import datetime
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.template.defaultfilters import truncatewords
from events.models import Event


class UpcomingEventsFeed(Feed):
    title = "Learn Aerial Upcoming Events NYC"
    link = "/events/feed"
    description = "Upcoming aerial events in New York City"

    def items(self):
        today = datetime.date.today()
        sixdays = today + datetime.timedelta(days=6)
        return Event.objects.filter(ongoing=False, published=True, start_date__gte=today, start_date__lte=sixdays).order_by('start_date')

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        truncated_description = truncatewords(item.description, 50)
        return truncated_description

    def item_pubdate(self, item):
        return datetime.datetime.combine(item.start_date, datetime.time())
