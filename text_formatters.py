from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import app, ctrl, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string
import re


WORD_SUBSTITUTES = {
    '.': 'point',
    'e-mail': 'email',
}


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
    word = WORD_SUBSTITUTES.get(word, word)
    return word


def join_words(words, sep=' '):
    out = ''
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out


def parse_words(m):
    top_level_words = list(map(parse_word, m.dgndictation[0]._words))

    all_words = []
    for word in top_level_words:
        # Dragon treats groups of words like 'top-level' and 'United States of
        # America' as a single word. Split it so we don't get spaces in our
        # variable names that we are trying to dictate
        all_words.extend(re.split(r'\s|-', word))

    return all_words


def insert(s):
    Str(s)(None)


def word(m, transformer=lambda word: word.lower()):
    text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
    text = WORD_SUBSTITUTES.get(text, text)
    insert(transformer(text))


def title_case_capitalize_word(index, word, _):
    words_to_keep_lowercase = (
        'a,an,the,at,by,for,in,is,of,on,to,up,and,as,but,or,nor'.split(',')
    )
    if index == 0 or word not in words_to_keep_lowercase:
        return word.capitalize()
    else:
        return word


formatters = {
    # e.g. 'hello world'
    'nat-way': (True, lambda i, word, _: word if i == 0 else ' ' + word),
    # e.g. 'HELLO WORLD'
    'upper-nat-way': (True, lambda i, word, _: word.upper() if i == 0 else ' ' + word.upper()),
    # e.g. 'hello world '
    'spay-way': (True, lambda i, word, _: word + ' '),
    # e.g. 'hello-world'
    'spine-way': (True, lambda i, word, _: word if i == 0 else '-' + word),
    # e.g. 'helloWorld'
    'camel': (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    # e.g. 'hello/world'
    'relpath': (True, lambda i, word, _: word if i == 0 else '/' + word),
    # e.g. 'hello.world'
    'dotway': (True, lambda i, word, _: word if i == 0 else '.' + word),
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
    'title': (False, title_case_capitalize_word),
    # e.g. 'hello, world'
    'params': (True, lambda i, word, _: word if i == 0 else ', ' + word),
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
    '(word | would) <dgnwords>': word,
    'snake <dgnwords>': lambda m: word(m, lambda w: w.capitalize()),
    'upper word <dgnwords>': lambda m: word(m, lambda w: w.upper()),

    '(%s) <dgndictation>++' % (' | '.join(formatters)): FormatText,
})
