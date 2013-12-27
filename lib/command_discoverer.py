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
import glob
import os
import sys
from os.path import basename

from constants import COOP_COMMAND_PATH


CURRENT_PATH = os.path.abspath(__file__).partition(os.path.basename((__file__)))[0]


def discover_commands(main_path):
    """Given path return name of files ending with .py."""
    files_on_path = glob.glob(os.path.join(main_path, COOP_COMMAND_PATH, "*.py"))
    return map(lambda x:basename(x).split(".py")[0],files_on_path)

def import_command(main_path, command_name):
    """Import command from name."""
    sys.path.append(main_path)
    return __import__(command_name)
