from django.conf import settings
from django.contrib.sites.models import Site
from kibrit import Kibrit


def context_processor(request):
    '''
    A context processor to add the "current site" to the current Context
    '''
    try:
        return {
            'REVISION': Kibrit().revision,
        }
    except :
        return {'REVISION':''} # an empty string