
class LanguageInvalidException(Exception):
    def __init__(self, lang):
        self._lang = lang

    def __str__(self):
        return f'LanguageError: {type(self._lang)}'


class ParametersInvalidException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'ParametersInvalidError'


class CommandInvalidException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'CommandInvalidError'


class ExecuteInvalidException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'ExecuteInvalidError'
