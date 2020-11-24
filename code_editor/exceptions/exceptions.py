class FileInvalidException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return f'LanguageError: {type(self._lang)}'


class DataBaseException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'ParametersInvalidError'