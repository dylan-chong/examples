from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import app, ctrl, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

# cleans up some Dragon output from <dgndictation>
mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
}
# used for auto-spacing
punctuation = set('.,-!?')

def parse_word(word):
    word = str(word).lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def join_words(words, sep=' '):
    out = ''
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out

def parse_words(m):
    return list(map(parse_word, m.dgndictation[0]._words))

def insert(s):
    Str(s)(None)

def word(m):
    text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
    insert(text.lower())

formatters = {
    'natword': (True, lambda i, word, _: word if i == 0 else ' '+word),
    'spaywid': (True, lambda i, word, _: word+' '),
    'camel': (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    'relpath': (True, lambda i, word, _: word if i == 0 else '/'+word),
    'dotword': (True, lambda i, word, _: word if i == 0 else '.'+word),
    'score': (True, lambda i, word, _: word if i == 0 else '_'+word),
    'upper-score': (True, lambda i, word, _: (word if i == 0 else '_'+word).upper()),
    'jumble': (True, lambda i, word, _: word),
    'sentence': (True, lambda i, word, _: word.capitalize() if i == 0 else " "+word),
    'proper': (True, lambda i, word, _: word.capitalize()),
    'title': (False, lambda i, word, _: word.capitalize()),
}

def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    try:
        words = parse_words(m)
    except AttributeError:
        with clip.capture() as s:
            press('cmd-c')
        words = s.get().split(' ')
        if not words:
            return

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words)-1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)

def copy_bundle(m):
    bundle = ui.active_app().bundle
    clip.set(bundle)
    app.notify('Copied app bundle', body='{}'.format(bundle))

ctx = Context('input')
ctx.keymap({
    'word <dgnwords>': word,

    '(%s) [<dgndictation>]' % (' | '.join(formatters)): FormatText,

    # more keys and modifier keys are defined in basic_keys.py

    'copy active bundle': copy_bundle,
})
