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
import unittest

from doit.task import dict_to_task
from mock import MagicMock, patch, call

from coop.main import CoopTaskLoader, DEFAULT_TASK_LOADER_CONFIG


class DummyPluginObject1(object):
    params = [{'name':'param1',
               'long':'param1',
               'short':'p',
               'default':'default value'}]

    def handle(self, *args, **kwargs):
        pass


class DummyPluginObject2(object):
    params = [{'name':'param1',
               'long':'param1',
               'short':'p',
               'default':'default value'}]

    def handle(self, *args, **kwargs):
        pass

DUMMY_DESCRIPTION_1 = 'dummy_description_1'
DUMMY_DOC_1 = 'dummy_doc_1'
DUMMY_NAME_1 = 'dummy_name_1'

DUMMY_DESCRIPTION_2 = 'dummy_description_2'
DUMMY_DOC_2 = 'dummy_doc_2'
DUMMY_NAME_2 = 'dummy_name_2'


class DummyPluginInfo1(object):
    description = DUMMY_DESCRIPTION_1
    doc = DUMMY_DOC_1
    name = DUMMY_NAME_1
    plugin_object = DummyPluginObject1()


class DummyPluginInfo2(object):
    description = DUMMY_DESCRIPTION_2
    doc = DUMMY_DOC_2
    name = DUMMY_NAME_2
    plugin_object = DummyPluginObject2()


class TestCoopTaskLoader(unittest.TestCase):
    def test_given_commands_are_present_when_calling_load_tasks_return_task_list(self):

        with patch('yapsy.PluginManager.PluginManager.getAllPlugins',
                   MagicMock(return_value=[DummyPluginInfo1,
                                           DummyPluginInfo2])) as mock_manager:
            tasks = CoopTaskLoader.load_tasks()

            dpo1 = DummyPluginObject1()
            dpo2 = DummyPluginObject2()

            task_1 = dict_to_task({
            'params': dpo1.params,
            'name': DummyPluginInfo1.name,
            'actions': [dpo1.handle],
            'doc': DummyPluginInfo1.description,
            })

            task_2 = dict_to_task({
            'params': dpo2.params,
            'name': DummyPluginInfo2.name,
            'actions': [dpo2.handle],
            'doc': DummyPluginInfo2.description,
            })

            expected_result = [[task_1, task_2], DEFAULT_TASK_LOADER_CONFIG]

            for i in range(len(tasks)):
                self.assertEqual(expected_result[0][i].name, tasks[0][i].name)
                self.assertEqual(expected_result[0][i].doc, tasks[0][i].doc)

            self.assertEqual(expected_result[1], tasks[1])

    def test_given_no_commands_are_present_when_calling_load_tasks_return_empty_list(self):

        with patch('yapsy.PluginManager.PluginManager.getAllPlugins',
                   MagicMock(return_value=[])) as mock_manager:
            tasks = CoopTaskLoader.load_tasks()

            expected_result_tasks = []

            self.assertEqual(expected_result_tasks, tasks[0])
            self.assertEqual(DEFAULT_TASK_LOADER_CONFIG, tasks[1])

if __name__ == '__main__':
    unittest.main()
