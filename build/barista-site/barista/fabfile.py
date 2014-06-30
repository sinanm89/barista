from fabric.api import *
from fabric.contrib.files import exists
from fabtools.vagrant import vagrant

@task
def eles(something='~'):
    run("ls %s" % something)
