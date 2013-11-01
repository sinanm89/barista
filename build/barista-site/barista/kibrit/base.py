import os
from subprocess import Popen, PIPE
from django.core.mail import mail_admins, send_mail
import sys
from barista import settings
from os import getcwd, name

LEGACY_LISTING_CACHE_PREFIX = "kibrit_"

class GitException(Exception):
    pass


class GitRevision(object):

    @property
    def revision(self):
        """
        Get current revision
        """
        return self.init_repo()

    def __init__(self, path=None):
        """
        Set and explicit path or try to find your own
        """
        self.path = path or self.find_git()


    def init_repo(self):
        """
        The command to run and tag to return
        """
        try:
            self._tag = self.git('git describe --always --tags')
            return self._tag
        except GitException:
            # TODO: Logger
            notify_admins(exception="Git Exception in init_repo()")

    def git(self, command=None, stderr=PIPE, stdout=PIPE, **kwargs):
        """
        Run a subprocess for the git command. Mail admins in the event of an error.
        """
        try:
            # POpen because check_output is 2.7 and Popen exists in 2.6.5
            proc = Popen(
                command.split(), stderr=stderr, stdout=stdout,
                close_fds=(name == 'posix'), cwd=self.path, **kwargs)

        except GitException:
            notify_admins(exception="Exception in git()")
        stdout, stderr = [s.strip() for s in proc.communicate()]
        status = proc.returncode
        if status:
            notify_admins(exception="Git Exception")
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
        except:
            notify_admins(exception="Exception in find_git()")

        output, error = [s.strip() for s in proc.communicate()]
        status = proc.returncode
        if status:
            subject="[Kibrit] Couldn't find .git directory"
            message="I couldn't find .git while trying to run %s I got status <%s> and error <%s> the output was <%s>"\
                    %(command, status, error, output)
            notify_admins(subject=subject,message=message)
        return output

def notify_admins(subject=None, message=None, exception=None):
    # if not settings.DEBUG:
    subject = subject or "[Kibrit] Kibrit has failed."
    message = message or "In project Something Kibrit has failed. Exception is : <%s>" %exception or 'Not Available'
    try:
        # send_mail("B", "A", "sinanm89@gmail.com", ["sinanm89@gmail.com"], fail_silently=True)
        mail_admins(subject, message, fail_silently=True)
    except:
        pass

