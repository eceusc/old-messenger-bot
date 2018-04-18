# help.py

from slack.modules import __all__ as commands
import sys

def process(words):
    s = 'List of commands: \n'

    for cmd in commands:
        if hasattr(sys.modules['slack.modules.' + cmd], 'help'):
            cmd_help = sys.modules['slack.modules.' + cmd].help
            s += '*{}* - {}\n'.format(cmd, cmd_help)
        else:
            s += '*{}* - [no help text]\n'.format(cmd)

    s += 'e.g. "/eceusc galex ahnaf"'
    return s
