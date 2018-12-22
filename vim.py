from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('vim')
ctx.keymap({
    'align (par|paragraph)': 'gwip',
    'save': Key('escape : w enter'),
    'exit file': Key(': q enter'),
    'force save': Key('escape : w ! enter'),
    'save exit':  Key('escape : w q enter'),
    'save all':   Key('escape : w a enter'),
    'move line up': 'ddkP',
    'move line down': 'ddp',
    'change word': 'ciw',
    'switch split': Key('ctrl-w ctrl-w'),

    # Tags
    '(jump deaf|jump to definition)': Key('ctrl-]'),
    'jump back': Key('ctrl-t'),
})
