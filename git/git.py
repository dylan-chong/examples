from talon.voice import Word, Context, Key, Rep, Str, press
#  from .git_commands import all_commands

#  # TODO merge below
#  command_map = {
    #  command.word_format(): command.execution_callback
    #  for command in all_commands
#  }

#  ctx = Context('git')
#  ctx.keymap(command_map)


if 1:
    # TODO NEXT find out how this is going to work
    def callback(m):
        pass#TODO

    ctx = Context('git')
    ctx.keymap({
        'git status ("branch"|"short")*': callback
    })
