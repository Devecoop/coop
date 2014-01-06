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
import sys

from doit.task import dict_to_task
from doit.cmd_base import TaskLoader
from doit.doit_cmd import DoitMain
from doit.cmd_help import Help as DoitHelp
from yapsy.PluginManager import PluginManager

from coop.lib.constants import BASE_COMMAND_PATH
COOP_VERSION = "0.1"

# Build the manager
simplePluginManager = PluginManager()
# Tell it the default place(s) where to find plugins
simplePluginManager.setPluginPlaces([BASE_COMMAND_PATH])
# Load all plugins
simplePluginManager.collectPlugins()


DEFAULT_TASK_LOADER_CONFIG = {'verbosity': 2}

class CoopTaskLoader(TaskLoader):

    @staticmethod
    def load_tasks(cmd=None, opt_values=None, pos_args=None):

        #task_list = [dict_to_task(param_task)]
        task_list = []

        for plugin_info in simplePluginManager.getAllPlugins():
            task_dict = {
            'params': plugin_info.plugin_object.params,
            'name': plugin_info.name,
            'actions': [plugin_info.plugin_object.handle],
            'doc': plugin_info.description,
            }

            new_task = dict_to_task(task_dict)

            task_list.append(new_task)

        return task_list, DEFAULT_TASK_LOADER_CONFIG


HELP_LINE_1 = "Coop is a tool to publish and socialize python projects http://getcoop.com\n\n"
HELP_LINE_2 = "Available commands:"
HELP_COMMAND_PATTERN = "  coop %-*s %s"
HELP_LINE_3 = ""
HELP_LINE_4 = "  coop version              show coop version"
HELP_LINE_5 = "  coop help                 show help / reference"
HELP_LINE_6 = "  coop help <command-name>  show command usage"



class Help(DoitHelp):
    """Show coop usage instead of doit """

    @staticmethod
    def print_usage(cmds):
        """Print coop "usage" (basic help) instructions."""
        print(HELP_LINE_1)
        print(HELP_LINE_2)

        tasks = CoopTaskLoader.load_tasks()

        for cmd in sorted(tasks[0]):
            print(HELP_COMMAND_PATTERN % (20, cmd.name, cmd.doc))

        print(HELP_LINE_3)
        print(HELP_LINE_4)
        print(HELP_LINE_5)
        print(HELP_LINE_6)


class Coop(DoitMain):
    # overwite help commands
    __version__ = COOP_VERSION
    DOIT_CMDS = list(DoitMain.DOIT_CMDS) + [Help]
    TASK_LOADER = CoopTaskLoader

    def get_commands(self):
        """Remove all doit commands."""
        commands = super(Coop, self).get_commands()
        commands.pop('dumpdb')
        commands.pop('strace')
        commands.pop('auto')
        commands.pop('clean')
        commands.pop('list')
        commands.pop('ignore')
        commands.pop('forget')
        return commands

    def run(self, cmd_args):
        """Override run method of doit so we can get a custom behavior."""
        sub_cmds = self.get_commands()
        args = self.process_args(cmd_args)

        tasks = CoopTaskLoader.load_tasks()

        if len(args) == 0 or any(arg in ["--help", '-h'] for arg in args):
            cmd_args = ['help']
            args = ['help']
            sub_cmds.pop('run')
        elif args[0] == 'version':
            self.print_version()
            return 0
        elif args[0] == 'run':
            cmd_args = ['help']
            args = ['help']
            sub_cmds.pop('run')

        elif not any(arg in [t.name for t in tasks[0]] for arg in args):
            cmd_args = ['help']
            args = ['help']
            sub_cmds.pop('run')

        return super(Coop, self).run(cmd_args)

    def print_version(self):
        """Print current coop version."""
        print("Coop version " + self.__version__)

def main(args):
    sys.exit(Coop(CoopTaskLoader()).run(args))
