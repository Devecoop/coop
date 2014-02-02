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

from invewrapper.invewrapper import mkvirtualenv
from skeleton import Skeleton, Var
from yapsy.IPlugin import IPlugin

from coop import settings

def sanitize_project_name(project_name):
    """Return a valid python project name."""
    return project_name


THIS_FILE_DIR = os.path.dirname(__file__)
PROJECT_TEMPLATES_DIR = os.path.join(THIS_FILE_DIR,
                                      'project-templates')

PROJECT_TEMPLATE_SPHINX = 'sphinx-package'
VAR_PROJECT_NAME = 'project_name'
VAR_AUTHOR = settings.SETTING_VAR_AUTHOR
VAR_AUTHOR_EMAIL = settings.SETTING_VAR_AUTHOR_EMAIL

MSG_ERROR_MODULE_PROJECT_NAME_NOT_GIVEN = """Project name not given, you must provide a project name."""

def BasicModule(project_name=None):
    if project_name is None:
        raise ValueError(MSG_ERROR_MODULE_PROJECT_NAME_NOT_GIVEN)

    class BasicModule(Skeleton):
        """
        Create an empty module with its setup script and a README file.
        """
        src = os.path.join(PROJECT_TEMPLATES_DIR, 'basic-module')
        variables = [
            Var(VAR_PROJECT_NAME, default=project_name),
            Var(VAR_AUTHOR, default=settings.config.get(VAR_AUTHOR)),
            Var(VAR_AUTHOR_EMAIL, default=settings.config.get(VAR_AUTHOR_EMAIL)),
            ]

    return BasicModule

def create_project(project_name, template=PROJECT_TEMPLATE_SPHINX):
    """Giving a project name, create a virtualenv and a project dir from a template."""
    s_project_name = sanitize_project_name(project_name)
    # TODO: add coop as a dependency when is ready
    mkvirtualenv(project_name, packages=['pew', 'skeleton', 'virtualenvwrapper']) # add coop
    BasicModule(s_project_name).cmd([s_project_name])
    # TODO: check wich commands pew uses to set project with an existing env
    #pew-setproject


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
