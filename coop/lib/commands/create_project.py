#  Coop a tool to deploy and socialize Python projects
#   Copyright (C) 2014  Juan Manuel Schillaci
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
# Coop version 0.1, Copyright (C) 2013  Juan Manuel Schillaci
#   Coop comes with ABSOLUTELY NO WARRANTY.
#   This is free software, and you are welcome to redistribute it
#   under certain conditions;
import os
import sys
from subprocess import Popen, PIPE, STDOUT, call

from yapsy.IPlugin import IPlugin
from skeleton import Skeleton, Var
from invewrapper.invewrapper import mkvirtualenv

def sanitize_name(name):
    return name


THIS_FILE_DIR = os.path.dirname(__file__)
PROJECT_TEMPLATES_DIR = os.path.join(THIS_FILE_DIR,
                                      'project-templates')

PROJECT_TEMPLATE_SPHINX = 'sphinx-package'
VAR_PROJECT_NAME = 'project_name'
VAR_AUTHOR = 'author'
VAR_AUTHOR_EMAIL = 'author_email'


class BasicModule(Skeleton):
    """
    Create an empty module with its setup script and a README file.
    """
    src = os.path.join(PROJECT_TEMPLATES_DIR, 'basic-module')
    variables = [
        Var(VAR_PROJECT_NAME),
        Var(VAR_AUTHOR),
        Var(VAR_AUTHOR_EMAIL),
        ]


def create_project(project_name, template=PROJECT_TEMPLATE_SPHINX):
    """Giving a project name, create a virtualenv and a project dir from a template."""
    mkvirtualenv(project_name, packages=['pew', 'skeleton', 'virtualenvwrapper']) # add coop


class Command(IPlugin):
    params = [{'name':'Project template',
                'long':'type',
                'short':'t',
                'default':'lib'},

                {'name':VAR_PROJECT_NAME,
                'long': VAR_PROJECT_NAME,
                 'default':None}
                ]

    def handle(self, *args, **kwargs):
        project_name = kwargs.get(VAR_PROJECT_NAME)
        create_project(project_name)
