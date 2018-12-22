from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('programming')

ctx.keymap({
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
})
