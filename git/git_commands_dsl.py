import re


class GitCommandRuleBuilder:
    def __init__(self, **data):
        if 'options' not in data:
            data['options'] = dict()
        self.data = data

    def option(self, alias, option, prepend_space=True):
        '''Defines an option for this git command.

        alias -- word for the user to say to trigger this option (string)
        option -- text to be outputted (anything executable in a Talon keymap,
            or a list of such)
        prepend_space -- whether to put a space before this option to space it
            from the previous option the user said (default True)
        '''
        alias = alias.strip()

        if alias in self.data['options']:
            return

        if isinstance(option, list):
            result_mapping = option
        else:
            result_mapping = [option]

        if prepend_space:
            result_mapping = [' '] + result_mapping

        self.data['options'][alias] = result_mapping
        return self

    def _smart_option(self, option, **keyword_arguments):
        '''``smart_options`` is the alternative to ``option``.
        Accepts a variety of inputs, and converts them into an appropriate
        format for dictation. For example, all of the following are valid:

        ``['.', '-', '--', 'some-option', '--another-option',
        '--[no-]using-the-thing', 'something/else']``

        Note that the user must say 'slash' if there is a '/' in the option.
        '''

        optional_pattern = r'-(.*)\[(.+)?\](.*)'

        if option == '.':
            alias = 'dot'
        elif re.match(r'^-+$', option):
            # TODO change to double dash to avoid conflicts between the
            # different number of dashes
            alias = 'dash ' * len(option)
        elif re.match(optional_pattern, option):
            # For example, option = '--[no-]progress'
            return self.smart_options([
                # For example, '--no-progress'
                re.sub(optional_pattern, r'-\1\2\3', option, count=1),
                # For example, '--progress'
                re.sub(optional_pattern, r'-\1\3', option, count=1),
            ], **keyword_arguments)
        else:
            alias = option
            alias = re.sub(r'/', ' slash ', alias)
            alias = re.sub(r'[^a-zA-Z0-9]', ' ', alias)

        return self.option(alias, option, **keyword_arguments)

    def smart_options(self, options, **keyword_arguments):
        '''See documentation for _smart_option()'''

        for option in options:
            self._smart_option(option, **keyword_arguments)

        return self

    # Defines a should a way to say (a bunch of) arguments
    convenience_option = option

    def apply(self, function):
        function(self)
        return self

    def build(self):
        return GitCommandRule(**self.data),
