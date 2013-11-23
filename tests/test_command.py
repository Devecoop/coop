#  Coop a tool to deploy and socialize Python projects
#   Copyright (C) 2013  Juan Manuel Schillaci
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
import unittest

from coop.lib.command_discoverer import discover_commands
from coop.lib.constants import COOP_COMAND_PATH

CURRENT_PATH = os.path.abspath(__file__).partition(__file__)[0]
COOP_TEST_COMMAND_PATH = os.path.join(CURRENT_PATH, COOP_COMAND_PATH)


class TestCommandDiscover(unittest.TestCase):
    def setUp(self):
        # Ensure .coop directory is empty before running the tests
        try:
            os.rmdir(COOP_TEST_COMMAND_PATH)
        except OSError:
            pass

    def test_given_no_files_are_present_then_return_empty_list(self):
        os.mkdir(COOP_TEST_COMMAND_PATH)
        expected_result = []
        result = discover_commands(CURRENT_PATH)
        self.assertEqual(expected_result, result)
        os.rmdir(COOP_TEST_COMMAND_PATH)


if __name__ == '__main__':
    unittest.main()
