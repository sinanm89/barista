from barista.kibrit.base import GitRevision


def revision(request):
    '''
    A context processor to add the "current site" to the current Context
    '''
    try:
        return {
            'REVISION': GitRevision().revision,
        }
    except:
        return {'REVISION':''} # an empty string