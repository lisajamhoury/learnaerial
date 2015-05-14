import facebook

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from events.models import Event 

class Command(BaseCommand):
    help = 'Posts unposted events to Facebook'

    def handle(self, *args, **options):
        print "running facebook autoposter"
        graph = facebook.GraphAPI(settings.FACEBOOK_PAGE_TOKEN)

        events_to_post = Event.objects.filter(post_to_facebook=True, posted_to_facebook=False)

        for event in events_to_post:
            if event.ready_to_post():
            	print "posted event: %s" % event 
                graph.put_object(settings.FACEBOOK_PAGE_ID, "feed", link=event.get_full_url()) 
                event.posted_to_facebook = True
                event.save()