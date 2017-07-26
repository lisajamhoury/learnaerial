from us.states import STATES

from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from django.utils.text import slugify

from listings.models import State


class Command(BaseCommand):
    def handle(self, *args, **options):
    	for state in STATES:
    		# import pdb; pdb.set_trace()
    		state_name = state.name
    		state_slug = slugify(state)
    		new_state, created = State.objects.get_or_create(
    			name=state_name,
    			slug=state_slug,
    		)

    		if created:
    			print 'Created new state %s' % new_state
    		else:
    			print 'Found existing state %s' % new_state
        