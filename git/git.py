from talon.voice import Word, Context, Key, Rep, Str, press
from git_commands import all_commands

# TODO merge below
command_map = {
    command.word_format(): command.execution_callback
    for command in all_commands
}

ctx = Context('git')
ctx.keymap(command_map)
