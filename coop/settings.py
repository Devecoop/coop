# -*- coding: utf-8 -*-
import ConfigParser
import os
import sys

HOME_DIRECTORY = os.getenv('HOME')
CONFIG_FILE_LOCATION = os.path.join(HOME_DIRECTORY, '.config', 'coop',
                                    'coop.conf')
SETTING_VAR_AUTHOR = 'author'
SETTING_VAR_AUTHOR_EMAIL = 'author_email'

config_parser = ConfigParser.RawConfigParser()


def _get_config():
    conf_file_present = os.path.isfile(CONFIG_FILE_LOCATION)

    try:
        if conf_file_present:
            config_parser.read(CONFIG_FILE_LOCATION)
        else:
            raise Exception
    except:
        print u"The config file is not present please create one at ~/config/coop/coop.conf"
        sys.exit()


    AUTHOR = config_parser.get('main', SETTING_VAR_AUTHOR)
    AUTHOR_EMAIL = config_parser.get('main', SETTING_VAR_AUTHOR_EMAIL)

    return {
        SETTING_VAR_AUTHOR: AUTHOR,
        SETTING_VAR_AUTHOR_EMAIL: AUTHOR_EMAIL
    }

config = _get_config()
if __name__ == '__main__':
    print config
