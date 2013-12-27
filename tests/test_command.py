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
import shutil
import unittest

from coop.lib.command_discoverer import discover_commands, import_command
from coop.lib.constants import COOP_COMMAND_PATH

CURRENT_PATH = os.path.abspath(__file__).partition(os.path.basename((__file__)))[0]
COOP_TEST_COMMAND_PATH = os.path.join(CURRENT_PATH, COOP_COMMAND_PATH)
DUMMY_COMMAND_1 = 'dummy1'
DUMMY_COMMAND_2 = 'dummy2'
DUMMY_COMMAND_3 = 'dummy3'
COMMAND_EXTENSION_SUFFIX = ".py"
COMMAND_EXTENSION_WRONG_SUFFIX = ".pyc"

DUMMY_COMMAND_1_PATH = os.path.join(COOP_TEST_COMMAND_PATH,
                                    DUMMY_COMMAND_1 + COMMAND_EXTENSION_SUFFIX)

DUMMY_COMMAND_2_PATH = os.path.join(COOP_TEST_COMMAND_PATH,
                                    DUMMY_COMMAND_2 + COMMAND_EXTENSION_SUFFIX)

DUMMY_COMMAND_3_PATH = os.path.join(COOP_TEST_COMMAND_PATH,
                                    DUMMY_COMMAND_3 + COMMAND_EXTENSION_SUFFIX)

DUMMY_COMMAND_WRONG_4_PATH = os.path.join(COOP_TEST_COMMAND_PATH,
                                    DUMMY_COMMAND_3 + COMMAND_EXTENSION_WRONG_SUFFIX)

TEST_COMMAND = """
class TestCommand(object):
    def handle(self):
        return True
"""


class TestRegisterCommand(unittest.TestCase):
    def test_given_valid_command_when_calling_register_command_return_imported_module(self):
        try:
            if not os.path.exists(COOP_TEST_COMMAND_PATH):
                os.mkdir(COOP_TEST_COMMAND_PATH)
            fp1 = open(DUMMY_COMMAND_1_PATH, "wb")
            fp1.write(TEST_COMMAND)
            fp1.close()

            commands = discover_commands(CURRENT_PATH)
            for command in commands:
                module = import_command(COOP_TEST_COMMAND_PATH, command)
            self.assertEqual(DUMMY_COMMAND_1, module.__name__)
        finally:
            shutil.rmtree(COOP_TEST_COMMAND_PATH)



class TestDiscoverCommand(unittest.TestCase):
    def setUp(self):
        # Ensure .coop directory is empty before running the tests
        try:
            os.rmdir(COOP_TEST_COMMAND_PATH)
        except OSError:
            pass

    def test_given_no_files_are_present_when_calling_discover_commands_return_empty_list(self):
        try:
            if not os.path.exists(COOP_TEST_COMMAND_PATH):
                os.mkdir(COOP_TEST_COMMAND_PATH)
            expected_result = []
            result = discover_commands(CURRENT_PATH)
            self.assertEqual(expected_result, result)
        finally:
            os.rmdir(COOP_TEST_COMMAND_PATH)

    def test_given_files_are_present_when_calling_discover_commands_return_list_with_file_names(self):
        try:
            if not os.path.exists(COOP_TEST_COMMAND_PATH):
                os.mkdir(COOP_TEST_COMMAND_PATH)
            fp1 = open(DUMMY_COMMAND_1_PATH, "wb")
            fp1.close()
            fp1 = open(DUMMY_COMMAND_2_PATH, "wb")
            fp1.close()
            fp1 = open(DUMMY_COMMAND_3_PATH, "wb")
            fp1.close()

            expected_result = [DUMMY_COMMAND_1, DUMMY_COMMAND_2,
                               DUMMY_COMMAND_3]
            result = discover_commands(CURRENT_PATH)
            self.assertEqual(expected_result.sort(), result.sort())
        finally:
            shutil.rmtree(COOP_TEST_COMMAND_PATH)

    def test_given_files_with_mixed_extensions_are_present_when_calling_discover_commands_return_only_valid_file_names(self):
        try:
            if not os.path.exists(COOP_TEST_COMMAND_PATH):
                os.mkdir(COOP_TEST_COMMAND_PATH)
            fp1 = open(DUMMY_COMMAND_1_PATH, "wb")
            fp1.close()
            fp1 = open(DUMMY_COMMAND_2_PATH, "wb")
            fp1.close()
            fp1 = open(DUMMY_COMMAND_WRONG_4_PATH, "wb")
            fp1.close()

            expected_result = [DUMMY_COMMAND_1, DUMMY_COMMAND_2]
            result = discover_commands(CURRENT_PATH)
            self.assertEqual(expected_result.sort(), result.sort())
        finally:
            shutil.rmtree(COOP_TEST_COMMAND_PATH)


if __name__ == '__main__':
    unittest.main()
