from code_editor.core.exceptions.exceptions import LanguageInvalidException


class NoneLanguageException(LanguageInvalidException):

    def __str__(self):
        return f'NoneLanguageError: {type(self._lang)}'


class TypeLanguageException(LanguageInvalidException):

    def __str__(self):
        return f'TypeLanguageError: {type(self._lang)} {self._lang}'


class FoundLanguageException(LanguageInvalidException):

    def __str__(self):
        return f'NoLanguageFoundError: {self._lang}'