import os
from subprocess import Popen, PIPE
from django.core.cache import cache
from django.core.mail import mail_admins, send_mail
import sys
from barista import settings
from os import getcwd, name


class GitRevision(object):

    _tag = None

    @property
    def revision(self):
        """
        Get current revision
        """
        self.init_repo()
        cache.set(self._tag, self._tag, 60)
        return self._tag

    def __init__(self, path=None):
        """
        If the kibrit tag is memcached then dont even try to get it
        Otherwise set the path through an explicit path or find on your own
        """
        cached_kibrit = cache.get(self._tag)
        if cached_kibrit:
            self._tag = cached_kibrit
        else:
            self.path = path or self.find_git()

    def init_repo(self):
        """
        The command to run and tag to return
        """
        try:
            self._tag = self.git('git describe --always --tags')
        except Exception, err: # TODO: Logging mechanism
            self._tag = ''

    def git(self, command=None, stderr=PIPE, stdout=PIPE, **kwargs):
        """
        Run a subprocess for the git command. Mail admins in the event of an error.
        """
        try:
            proc = Popen(
                command.split(), stderr=stderr, stdout=stdout,
                close_fds=(name == 'posix'), cwd=self.path, **kwargs)

        except Exception, err:
            pass
        stdout, stderr = [s.strip() for s in proc.communicate()]
        return stdout

    def find_git(self, **kwargs):
        """
        Recursively finds a file directory named .git
        """
        command = "find -L ../src/ -type d -name .git".split()
        command[2] = kwargs.get('path') or os.path.join(os.path.realpath(os.path.dirname(sys.argv[0])), '../src/')
        command[6] = kwargs.get('pattern') or command[6]
        try:
            proc = Popen(command, stderr=PIPE, stdout=PIPE,
                         close_fds=(name == 'posix'), cwd=os.path.dirname(command[2]), **kwargs)
        except Exception, err:
            pass
        output, error = [s.strip() for s in proc.communicate()]
        return output
