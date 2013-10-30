import os
from subprocess import Popen, PIPE
from django.core.mail import send_mail
from barista import settings
from os import getcwd, name


class GitException(Exception):
    pass


class Kibrit(object):

    @property
    def revision(self):
        """ Get current revision.

        :return str:

        """
        return self.init_repo()

    def __init__(self, path=None):
        """

        """
        self.path = path or os.path.join(os.path.realpath(os.path.dirname(".git"))) or getcwd()

    def init_repo(self):
        """ Initialize self repo.

        :return GitRepo:

        """
        try:
            self._tag = self.git('git describe --always --tags')
            return self._tag

        except GitException:
            # TODO: Logger
            print 'exception'
            notify_admins(exception="Git Exception")


            # raise TypeError(e)


    def git(self, command=None, stderr=PIPE, stdout=PIPE, **kwargs):
        """
        Run git command.
        If it runs into an exception notify admins
        """
        try:
            # POpen because check_output is 2.7 and Popen exists in 2.6.5
            proc = Popen(
                command.split(), stderr=stderr, stdout=stdout,
                close_fds=(name == 'posix'), cwd=self.path, **kwargs)

        except OSError:
            notify_admins(exception="OS ERROR")
        stdout, stderr = [s.strip() for s in proc.communicate()] # noqa
        status = proc.returncode

        # DEBUG
        #
        # print "--------PATH----------"
        # print self.path
        # print '-----STDOUT------'
        # print stdout
        # print status
        # print '------------------'

        if status:
            notify_admins(exception="Git Exception")
        return stdout





def notify_admins(message=None, exception=None):
    if not settings.DEBUG:
        subject = "[Kibrit] Kibrit has failed."
        message = message or "In project Something Kibrit has failed. Exception is : " + exception
        from_mail = settings.ADMINS
        to_mails = settings.ADMINS
        try:
            send_mail(subject, message, from_mail, to_mails, fail_silently=True)
        except:
            pass