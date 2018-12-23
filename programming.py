from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('programming')

ctx.keymap({
    # Programming Operators
    'compare equal': ' == ',
    'compare not equal': ' != ',
    'compare greater': ' > ',
    'compare less': ' < ',
    'compare greater equal': ' >= ',
    'compare less equal': ' <= ',
    'boolean or': ' || ',
    'boolean and': ' && ',
    'bitwise or': ' | ',
    'bitwise and': ' & ',
    'bitwise ex or': ' ^ ',
    'math times': ' * ',
    'math divide': ' / ',
    'math add': ' + ',
    'math minus': ' - ',
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
})
