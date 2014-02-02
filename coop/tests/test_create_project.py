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
import datetime
import unittest
from contextlib import nested

from coop.lib.commands.create_project import create_project, BasicModule, \
    VAR_PROJECT_NAME, MSG_ERROR_MODULE_PROJECT_NAME_NOT_GIVEN
from mock import MagicMock, patch

from coop.settings import SETTING_VAR_AUTHOR, SETTING_VAR_AUTHOR_EMAIL

DUMMY_PROJECT_NAME = 'dummyproj'
DUMMY_SETTING_AUTHOR = 'dummyauthor'
DUMMY_SETTING_AUTHOR_EMAIL = 'dummyauthoremail'

DUMMY_SETTINGS_DICT = {SETTING_VAR_AUTHOR: DUMMY_SETTING_AUTHOR,
                       SETTING_VAR_AUTHOR_EMAIL: DUMMY_SETTING_AUTHOR_EMAIL}

# TODO: Change tests to use a BDD framework


class CreateProjectDirectoryTestCase(unittest.TestCase):
    def test_given_project_name_and_no_template_when_calling_create_project_then_call_mkvirtualenv_and_basic_module_cmd_with_project_name(self):
        with nested(patch('coop.lib.commands.create_project.mkvirtualenv',
                   MagicMock()),
                    patch('coop.lib.commands.create_project.BasicModule',
                          MagicMock())
                          ) as (mock_mkv, mock_bmo):

            create_project(DUMMY_PROJECT_NAME)

            mock_mkv.assert_called_with(DUMMY_PROJECT_NAME,
                                 packages=['pew', 'skeleton',
                                               'virtualenvwrapper'])

            mock_bmo.assert_called_with(DUMMY_PROJECT_NAME)

    def test_given_no_project_name_and_no_template_when_calling_create_project_then_fail(self):
        self.assertRaises(TypeError, create_project)


# These scenarios assume that settings are always present
class BasicModuleFactoryTestCase(unittest.TestCase):
    def test_given_project_name_when_calling_BasicModule_then_return_skeleton_class_with_project_name_author_and_author_email_already_set(self):
        with patch('coop.lib.commands.create_project.settings.config', DUMMY_SETTINGS_DICT):
            basic_module_instance = BasicModule(DUMMY_PROJECT_NAME)()
            current_year = datetime.datetime.now().year

            expected_result_items = sorted([(SETTING_VAR_AUTHOR_EMAIL,
                                      DUMMY_SETTING_AUTHOR_EMAIL),
             (VAR_PROJECT_NAME, DUMMY_PROJECT_NAME),
             (SETTING_VAR_AUTHOR, DUMMY_SETTING_AUTHOR),
             ('year', current_year)])

            self.assertEqual(expected_result_items,
                             sorted(basic_module_instance.items()))


    def test_given_no_project_name_when_calling_BasicModule_then_raise_ValueError(self):

        with self.assertRaises(ValueError) as cm:
            BasicModule()

        expected_message = MSG_ERROR_MODULE_PROJECT_NAME_NOT_GIVEN
        self.assertEqual(expected_message, cm.exception.message)

if __name__ == '__main__':
    unittest.main()
