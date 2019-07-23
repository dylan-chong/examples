"""
Propietary commands for my workflow
"""

from talon.voice import Word, Context, Key, Rep, Str
import datetime
import time


def notes_complete_line(_):
    Key('cmd-right cmd-shift-left cmd-x backspace')(None)
    Key('cmd-down * space')(None)

    Str(str(datetime.datetime.now()))(None)
    Key('space cmd-v')(None)

    Key('cmd-up')(None)

    # Move cursor down to bulleted list (yes this is very propietary)
    Key('down')(None)
    Key('down')(None)
    Key('down')(None)


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


ctx = Context('random')
ctx.keymap({
    # tmux (assumes prefix key is control-s)
    'switch panes': Key('ctrl-s ; ctrl-s z'),

    'notes complete line': notes_complete_line,

    'short cat': [Key('cmd-shift-space'), lambda _: time.sleep(0.2)],

    'edit in vim': Key('cmd-a cmd-c cmd-ctrl-v'),

    'open in new tab': Key('cmd-c cmd-t cmd-v enter'),

    'do pause': lambda _: time.sleep(0.4),

    # Spotlight/Alfred stuff
    'clipboard': AlfredCommands.define('clipboard'),
    'clear notifications': AlfredCommands.define('clear notifications'),
    'toggle music': AlfredCommands.define('play'),
    'open app <dgndictation>': AlfredCommands.open_app,

    'jupiter run all': [
        Key('cmd-shift-f'),
        lambda _: time.sleep(0.1),
        'restart kernel and run all cells',
        Key('down down enter'),
    ],

    # TODO: get repeats working properly
    'triple back tick': '```',
})
