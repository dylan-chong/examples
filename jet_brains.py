from talon.voice import Word, Context, Key, Rep, Str, press
import time

ctx = Context('jet_brains')
ctx.keymap({
    'find (action|actions)': Key('cmd-shift-a'),
    'find (usages|uses)': Key('alt-f7'),
    'find (subclasses|subclass)': Key('cmd-alt-b'),
    'find in superclass': Key('cmd-u'),
    'find in (path|files)': Key('cmd-shift-f'),
    'do rename': Key('shift-f6'),
    'toggle breakpoint': Key('cmd-f8'),
    'file structure': Key('cmd-f12'),
})
