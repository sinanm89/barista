# setup(
#     name='django-geoportail',
#     version='0.3.1',
#     author=u'Bruno Renié',
#     author_email='bruno.renie.fr',
#     packages=['geoportal'],
#     url='http://bitbucket.org/bruno/django-geoportail',
#     license='BSD licence, see LICENCE.txt',
#     description='Add maps and photos from the French National Geographic' + \
#                 ' Institute to GeoDjango',
#     long_description=open('README.txt').read(),
#     zip_safe=False,
# )
#
# #!/usr/bin/env python
#
"""
Kibrit
------

SCM watcher tool. Get current revision and send update notify.
"""

import sys
from os import path as op

from setuptools import setup, find_packages


def read(fname):
    try:
        return open(op.join(op.dirname(__file__), fname)).read()
    except IOError:
        return ''


NAME = 'kibrit'

CURDIR = op.dirname(__file__)
MODULE = __import__(NAME)
README = op.join(CURDIR, 'README.rst')
REQUIREMENTS = open(op.join(CURDIR, 'requirements.txt')).readlines()

if sys.version_info < (2, 7):
    REQUIREMENTS.append('importlib')


setup(
    name=NAME,
    version=MODULE.__version__,
    license=MODULE.__license__,
    author=MODULE.__author__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    platforms=('Any'),
    keywords = "mercurial git static revision django flask".split(),

    author_email='horneds@gmail.com',
    url=' http://github.com/klen/dealer',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Environment :: Console',
    ],

    packages=find_packages(),
    install_requires=REQUIREMENTS,
    test_suite = 'tests',
    tests_require=('flask', 'mercurial', 'django'),
)