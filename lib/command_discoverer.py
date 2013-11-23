import os

from constants import COOP_COMAND_PATH


def discover_commands(main_path):
    files_on_path = os.listdir(os.path.join(main_path, COOP_COMAND_PATH))
    return files_on_path
