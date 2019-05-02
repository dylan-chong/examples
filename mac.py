from talon.voice import Word, Context, Key, Rep, Str, press
import time

ctx = Context('mac')
ctx.keymap({
    # Text editing
    'mac delete line': Key('cmd-right cmd-shift-left cmd-x backspace'),
    'mac line up': Key(
        'cmd-right cmd-shift-left cmd-x '
        'backspace cmd-left cmd-v enter up cmd-right'
    ),
    'mac line down': Key(
        'cmd-right cmd-shift-left cmd-x backspace down cmd-right enter cmd-v'
    ),
    'mac copy all': Key('cmd-a cmd-c'),
    'mac cut all': Key('cmd-a cmd-x'),
    'mac paste all': Key('cmd-a cmd-v'),

    # Random mac commands
    'spotlight': [Key('cmd-space'), lambda _: time.sleep(0.3)],
})
