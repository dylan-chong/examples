from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('programming')

ctx.keymap({
    # Programming Operators
    'compare equal': ' == ',
    'compare not equal': ' != ',
    'compare triple equal': ' === ',
    'compare triple not equal': ' !== ',
    'compare greater': ' > ',
    'compare less': ' < ',
    'compare greater equal': ' >= ',
    'compare less equal': ' <= ',
    'boolean or': ' || ',
    'boolean and': ' && ',
    'bitwise or': ' | ',
    'bitwise and': ' & ',
    'bitwise ex or': ' ^ ',
    'mat times': ' * ',
    'mat divide': ' / ',
    'mat add': ' + ',
    'mat minus': ' - ',
    'set value': ' = ',
    'set plus equal': ' += ',
    'set minus equal': ' -= ',
    'set times equal': ' *= ',
    'set divide equal': ' /= ',
    'lamb (dash|-)': ' -> ',
    'lamb eek': ' => ',
    'back (dash|-)': ' <- ',
    'pie opper': '|> ',  # sounds like 'pipe operator' for Elixir
    'slash comment': '// ',
    'pie dunder': '__',
    'define as': ' :: ',

    # Programming Keywords
    'key const': 'const',
    'key var': 'var',
    'key val': 'val',
    'key bool': 'bool',
    'key boolean': 'boolean',
    'key int': 'int',
    'key deaf': 'def',
    'key null': 'null',
    'key nil': 'nil',
    'key conned': 'cond',
    'key ee-lif': 'elif',

    # Terms/words that dragon has some difficulty understanding even after
    # manually correcting dragon to train it (or are convenience words)
    'term to do': 'TODO: ',
    'term to do next': 'TODO NEXT: ',
    'term to do after': 'TODO AFTER: ',
    'term to do sometime': 'TODO SOMETIME: ',
    'term to do later': 'TODO LATER: ',
    'term to do last': 'TODO LAST: ',
    'term whip': 'WIP ',
    'term snake git': 'Git',
    'term git': 'git',
    'term diff': 'diff',
    'term grep': 'grep',
    'term kotlin': 'kotlin',
    # It is difficult to get dragon to not interpret saying 'python' as
    # 'hyphen'
    'term python': 'python',
    'term cat': 'cat',  # Dragon has difficulty recognising this word
    'term upper jason': 'JSON',
    'term jason': 'json',
    'term in it': 'init',
    'term sync': 'sync',
    'term vim': 'vim',
})
