from talon.voice import Context, Str, press
import string

alpha_alt = 'share bat cot drum each fine gust harp site jury crunch look made need odd paint quench red sun trap urge vote whale plex yank zeal'.split()

f_keys = {f'F {i}': f'f{i}' for i in range(1, 13)}
# arrows are separated because 'up' has a high false positive rate
arrows = {
    'left': 'left',
    'right': 'right',
    'gup': 'up',
    'down': 'down',
}
simple_keys = {
    'tab': 'tab',
    'quit': 'escape',
    'enter': 'enter',
    'space': 'space',
    'home': 'home',
    'pageup': 'pageup',
    'pagedown': 'pagedown',
    'end': 'end',
}
alternate_keys = {
    'delete': 'backspace',
    'forward delete': 'delete',
}
symbols = {
    'question': '?',
    'dash': '-',
    'plus': '+',
    'equals': '=',
    'tilde': '~',
    'back tick': '`',
    'bang': '!',
    'dollar': '$',
    'underscore': '_',
    'semi': ';',
    'ratio': ':',

    'lacket': '[',
    'racket': ']',
    'push': '(',
    'pop': ')',
    'lace': '{',
    'race': '}',
    'langle': '<',
    'wrangle': '>',

    'aster': '*',
    'hash': '#',
    'percent': '%',
    'caret': '^',
    'at sign': '@',
    'ampersand': '&',
    'piper': '|',

    'dub quote': '"',
    'sing quote': "'",
    'point': '.',
    'comma': ',',
    'space': ' ',
    'slash': '/',
    'backslash': '\\',
}
modifiers = {
    'apple': 'cmd',
    'con': 'ctrl',
    'big': 'shift',
    'alter': 'alt',
    'mash mod': 'cmd-shift-ctrl',
}

alphabet = dict(zip(alpha_alt, string.ascii_lowercase))
digits = {str(i): str(i) for i in range(10)}
keys = {}
keys.update(f_keys)
keys.update(simple_keys)
keys.update(alternate_keys)
keys.update(symbols)

# map alnum and keys separately so engine gives priority to letter/number repeats
keymap = keys.copy()
keymap.update(arrows)
keymap.update(alphabet)
keymap.update(digits)

def insert(s):
    Str(s)(None)

def get_modifiers(m):
    try:
        return [modifiers[mod] for mod in m['basic_keys.modifiers']]
    except KeyError:
        return []

def get_keys(m):
    groups = ['basic_keys.keys', 'basic_keys.arrows', 'basic_keys.digits', 'basic_keys.alphabet']
    for group in groups:
        try:
            return [keymap[k] for k in m[group]]
        except KeyError: pass
    return []

def press_keys(m):
    mods = get_modifiers(m)
    keys = get_keys(m)
    if mods:
        press('-'.join(mods + [keys[0]]))
        keys = keys[1:]
    for k in keys:
        press(k)

ctx = Context('basic_keys')
ctx.keymap({
    '{basic_keys.modifiers}* {basic_keys.alphabet}+': press_keys,
    '{basic_keys.modifiers}* {basic_keys.digits}+': press_keys,
    '{basic_keys.modifiers}* {basic_keys.keys}+': press_keys,
    '{basic_keys.modifiers}* {basic_keys.arrows}+': press_keys,
})
ctx.set_list('alphabet', alphabet.keys())
ctx.set_list('arrows', arrows.keys())
ctx.set_list('digits', digits.keys())
ctx.set_list('keys', keys.keys())
ctx.set_list('modifiers', modifiers.keys())
