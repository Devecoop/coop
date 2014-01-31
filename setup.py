#!/usr/bin/env python

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

import os

from setuptools import setup, find_packages

PROJECT = 'coop'
VERSION = open('VERSION').read().strip()
URL = ''
AUTHOR = 'Juan Manuel Schillaci'
AUTHOR_EMAIL = 'juan.schillaci@devecoop.com'
DESC = 'Automation Build, Publish and Documentation tool for Python projects, Highly extensible'

def read_file(file_name):
    file_path = os.path.join(
        os.path.dirname(__file__),
        file_name
        )
    return open(file_path).read()

setup(
    name=PROJECT,
    version=VERSION,
    description=DESC,
    long_description=read_file('README'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=read_file('LICENSE'),
    namespace_packages=[],
    #packages=['coop', 'coop.lib', 'coop.tests'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[
        'https://github.com/stumitchell/skeleton#egg=skeleton'
    ],
    install_requires=[
        'skeleton',
        'virtualenvwrapper',
        'Yapsy==1.10.223',
        'argparse==1.2.1',
        'doit==0.24.0',
        'mock==1.0.1',
        'nose==1.3.0',
        'pyinotify==0.9.4',
        'six==1.5.1',
        'pew==0.1.9',

        # -*- Required files -*-
    ],
    entry_points = {
        'console_scripts':
            ['coop = coop.main:main']
    },
    classifiers=[
        # see http://pypi.python.org/pypi?:action=list_classifiers
        # -*- Classifiers -*-
        "Programming Language :: Python",
    ],
)
