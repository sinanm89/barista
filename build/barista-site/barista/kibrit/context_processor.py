from barista import settings
from barista.kibrit.base import GitRevision


def revision(request):
    '''
    A context processor to add the "current site" to the current Context
    '''
    try:
        return {
            'REVISION': GitRevision(settings.KIBRIT_PATH).revision,
            # 'REVISION': GitRevision(path="/home/vagrant/barista/src/barista").revision,
        }
    except:
        return {'REVISION':''} # an empty string