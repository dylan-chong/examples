"""
Propietary commands for my workflow
"""

from talon.voice import Context, Key, Str
import time


class AlfredCommands:
    @staticmethod
    def open_app(m):
        app_name_words = map(lambda word: word.word, m._words[2])
        app_name = ' '.join(app_name_words)
        AlfredCommands.run(app_name)

    @staticmethod
    def define(command):
        return lambda _: AlfredCommands.run(command)

    @staticmethod
    def run(command):
        Key('cmd-space')(None)
        time.sleep(0.2)
        Str(command)(None)
        time.sleep(0.2)
        Key('enter')(None)


def sleep(seconds):
    return lambda _: time.sleep(seconds)


def keys_with_delays(keys_string, delay=0.2):
    def execute(_):
        for key in keys_string.split(' '):
            Key(key)(None)
            time.sleep(delay)

    return execute


ctx = Context('random')
ctx.keymap({
    # tmux (assumes prefix key is control-s)
    'switch panes': Key('ctrl-s ; ctrl-s z'),

    'short cat': [Key('cmd-shift-space'), sleep(0.2)],

    'edit in vim': keys_with_delays('cmd-a cmd-c cmd-ctrl-v'),

    'open in new tab': keys_with_delays('cmd-c cmd-t cmd-v enter'),

    'do pause': sleep(0.4),

    # Spotlight/Alfred stuff
    'clipboard': AlfredCommands.define('clipboard'),
    'clear notifications': AlfredCommands.define('clear notifications'),
    'toggle music': AlfredCommands.define('play'),
    'open app <dgndictation>': AlfredCommands.open_app,

    'jupiter run all': [
        Key('cmd-shift-f'),
        sleep(0.1),
        'restart kernel and run all cells',
        Key('down down enter'),
    ],

    # TODO: get repeats working properly
    'triple back tick': '```',
    'triple dash': '---',

    'bib cite': [' \\cite{}', Key('left')],  # Useful in latex

    'rerun command': Key('ctrl-c ctrl-c up enter'),
})
