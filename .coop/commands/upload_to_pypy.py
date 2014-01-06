from yapsy.IPlugin import IPlugin


class Command(IPlugin):
    params = [{'name':'param1',
                'long':'param1',
                'short':'p',
                'default':'default value'},

                {'name':'param2',
                'long':'param2',
                'type': int,
                'default':0}]

    def handle(*args, **kwargs):
        print kwargs['param2']
        print "Creating egg"
        print "Uploading to pypy"
