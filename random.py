from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('random')
ctx.keymap({
    # tmux (assumes prefix key is control-s)
    'switch panes': Key('ctrl-s ; ctrl-s z'),
})
