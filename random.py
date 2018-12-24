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
    time.sleep(0.6)  # Give user chance to see what was typed

    Key('cmd-up')(None)


def run_alfred_command(command):
    return [
        Key('cmd-space'),
        lambda _: time.sleep(0.2),
        command,
        lambda _: time.sleep(0.2),
        Key('enter'),
    ]


def open_app(m):
    app_name_words = map(lambda word: word.word, m._words[2])
    app_name = ' '.join(app_name_words)

    Key('cmd-space')(None)
    time.sleep(0.2)
    Str(app_name)(None)
    time.sleep(0.2)
    Key('enter')(None)


ctx = Context('random')
ctx.keymap({
    # tmux (assumes prefix key is control-s)
    'switch panes': Key('ctrl-s ; ctrl-s z'),

    'notes complete line': notes_complete_line,

    'short cat': Key('cmd-shift-space'),

    'edit in vim': Key('cmd-a cmd-c cmd-ctrl-v'),

    'open in new tab': Key('cmd-c cmd-t cmd-v enter'),

    'clipboard': run_alfred_command('clipboard'),
    'clear notifications': run_alfred_command('clear notifications'),
    'toggle music': run_alfred_command('play'),
    'open app <dgndictation>': open_app,

    'jupiter run all': [
        Key('cmd-shift-f'),
        lambda _: time.sleep(0.1),
        'restart kernel and run all cells',
        Key('down down enter'),
    ],
})
