#!/usr/bin/env python
import os

from distutils.command.install import INSTALL_SCHEMES
from distutils.core import setup

root = os.path.abspath(os.path.dirname(__file__))
os.chdir(root)

VERSION = '0.61.2'

setup(name='django-olwidget',
    version=VERSION,
    description="OpenLayers mapping widget for Django",
    author='Charlie DeTar',
    author_email='cfd@media.mit.edu',
    url='http://olwidget.org',
    packages=['olwidget'],
    package_dir={'': 'django-olwidget'},
    package_data={
        'olwidget': [
            'static/olwidget/css/*',
            'static/olwidget/img/*',
            'static/olwidget/js/*',
            'templates/admin/*',
            'templates/olwidget/*'
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
