"""
Propietary commands for my workflow for notes app
"""

from talon.voice import Context, Key, Str
from talon import tap
from talon import ui
import datetime
import time


def on_key(typ, e):
    if ui.active_app().bundle != 'com.apple.Notes':
        return
    if e != 'ctrl-shift-cmd-c':
        return
    if not e.up:
        return

    e.block()

    #  time.sleep(0.3)
    notes_complete_line(None)


def notes_complete_line(_):
    Key('cmd-right cmd-shift-left cmd-x backspace')(None)
    Key('cmd-down cmd-v cmd-left space left')(None)

    Str(str(datetime.datetime.now()))(None)

    Key('cmd-up')(None)

    # Move cursor down to bulleted list (yes this is very propietary)
    Key('down')(None)
    Key('down')(None)
    Key('down')(None)


ctx = Context('notes', bundle='com.apple.Notes')
ctx.keymap({
    'notes complete line': notes_complete_line,
})

tap.register(tap.KEY | tap.HOOK, on_key)
