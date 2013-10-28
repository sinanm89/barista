import os
from subprocess import Popen
from django.views.generic import TemplateView
from django.template import RequestContext
from barista import settings
from os import getcwd

class BaristaHomeView(TemplateView):
    template_name = "base.html"
    # template_name = "examples/grid/index.html"
    def get(self, request, *args, **kwargs):
        print settings.STATIC_ROOT

        kit.kibrit()
        context = self.get_context_data(**kwargs)
        # return render_to_response('example.html',{},context_instance=RequestContext(request))
        return self.render_to_response(context)


class GitException(object):
    pass



class Kibrit(object):

    git_command = 'git'

    def __init__(self, path=None):
        self.path = path


    @property
    def path(self):
        self._path = getcwd() or os.path.join(os.path.realpath(os.path.dirname(".git")))
        return self._path


    def git(self, command=None, stderr=PIPE, stdout=PIPE, **kwargs):
        """ Run git command.

        :return str: The command output.

        """

        cmd = ' '.join((self.git_command, command))

        try:
            proc = Popen(
                cmd.split(), stderr=stderr, stdout=stdout,
                close_fds=(name == 'posix'), cwd=self.path, **kwargs)

        except OSError:
            raise GitException('Git not found.')

        stdout, stderr = [s.strip() for s in proc.communicate()] # noqa
        status = proc.returncode
        if status:
            raise GitException(stderr)

        return stdout

    def init_repo(self):
        """ Initialize self repo.

        :return GitRepo:

        """
        try:
            self._repo = self.git(self.path)
            self._revision = self.repo.git('log -1 --format=%h')
            self._tag = self.repo.git('describe --always --tags')
            return self._repo

        except GitException as e:
            if not self.options.get('silent'):
                logger.error(e)

            raise TypeError(e)

