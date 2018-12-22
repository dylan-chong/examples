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


ctx = Context('random')
ctx.keymap({
    # tmux (assumes prefix key is control-s)
    'switch panes': Key('ctrl-s ; ctrl-s z'),

    'notes complete line': notes_complete_line,

    'short cat': Key('cmd-shift-space'),
})
