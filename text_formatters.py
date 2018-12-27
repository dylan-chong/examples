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


def title_case_capitalise_word(index, word, _):
    words_to_keep_lowercase = (
        'a,an,the,at,by,for,in,of,on,to,up,and,as,but,or,nor'.split(',')
    )
    if index == 0 or word not in words_to_keep_lowercase:
        return word.capitalize()
    else:
        return word


formatters = {
    # e.g. 'hello world'
    'natword': (True, lambda i, word, _: word if i == 0 else ' ' + word),
    # e.g. 'hello world '
    'spaywid': (True, lambda i, word, _: word + ' '),
    # e.g. 'helloWorld'
    'camel': (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    # e.g. 'hello/world'
    'relpath': (True, lambda i, word, _: word if i == 0 else '/' + word),
    # e.g. 'hello.world'
    'dotword': (True, lambda i, word, _: word if i == 0 else '.' + word),
    # e.g. 'hello_world'
    'score': (True, lambda i, word, _: word if i == 0 else '_' + word),
    # e.g. 'HELLO_WORLD'
    'upper-score': (True, lambda i, word, _: (word if i == 0 else '_' + word).upper()),
    # e.g. 'helloworld'
    'jumble': (True, lambda i, word, _: word),
    # e.g. 'Hello world'
    'sentence': (True, lambda i, word, _: word.capitalize() if i == 0 else " " + word),
    # e.g. 'Hello world '
    'spaytince': (True, lambda i, word, _: word.capitalize() + " " if i == 0 else word + " "),
    # e.g. 'HelloWorld'
    'proper': (True, lambda i, word, _: word.capitalize()),
    # e.g. 'Hello World'
    'title': (False, title_case_capitalise_word),
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
            word = func(i, word.lower(), i == len(words)-1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)


ctx = Context('text_formatters')
ctx.keymap({
    'word <dgnwords>': word,

    '(%s) [<dgndictation>]' % (' | '.join(formatters)): FormatText,
})
