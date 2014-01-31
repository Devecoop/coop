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
import unittest

from coop.lib.commands.create_project import create_project
from mock import MagicMock, patch, call


DUMMY_PROJECT_NAME = 'dummyproj'


class CreateProjectDirectoryTestCase(unittest.TestCase):
    def test_given_project_name_when_calling_create_project_then_call_mkvirtualenv(self):
        with patch('invewrapper.invewrapper.mkvirtualenv',
                   MagicMock()) as mock_manager:

            create_project(DUMMY_PROJECT_NAME)
            expected_calls = [
                                call(DUMMY_PROJECT_NAME,
                                     packages=['pew', 'skeleton',
                                               'virtualenvwrapper'])
                              ]

            mock_manager.assert_has_calls(expected_calls)

if __name__ == '__main__':
    unittest.main()
