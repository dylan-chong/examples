from talon.voice import Word, Context, Key, Rep, Str, press
import time


def Sleep(delay):
    return lambda _: time.sleep(delay)


ctx = Context('vim')
ctx.keymap({
    # Files
    'save': [Key('escape'), Sleep(0.2), Key(': w enter')],
    'exit': Key(': q enter'),
    'force save': Key('escape : w ! enter'),
    'save all': Key('escape : w a enter'),

    # Tags
    '(jump deaf|jump to definition)': Key('ctrl-]'),
    'jump back': Key('ctrl-t'),

    'align (par|paragraph)': 'gwip',

    # tmux needs a delay to register an escape properly
    'quit': [Key('escape'), Sleep(0.2)],

    'move line gup': 'ddkP',
    'move line down': 'ddp',

    'change word': 'ciw',

    'switch split': Key('ctrl-w ctrl-w'),
})
