from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('vim')
ctx.keymap({
    'align (par|paragraph)': 'gwip',
    'save file': [Key('escape'), ':w', Key('enter')],
    'exit file': [':q', Key('enter')],
    'force save': [Key('escape'), ':w!', Key('enter')],
    'save exit': [Key('escape'), ':wq', Key('enter')],
    'save all [files]': [Key('escape'), ':wa', Key('enter')],
    'move line up': 'ddkP',
    'move line down': 'ddp',
    'change word': 'ciw',
    'switch split': Key('ctrl-w ctrl-w'),

    # Tags
    '(jump deaf|jump to definition)': Key('ctrl-]'),
    'jump back': Key('ctrl-t'),
})
