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
