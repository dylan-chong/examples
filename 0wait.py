# TEMP Hack to remove keys getting typed out of order
# TODO: remove this when the new api is out

from talon import voice

old_press = voice.press


def press(key, **kwargs):
    kwargs['wait'] = 4000
    return old_press(key, **kwargs)


voice.press = press
