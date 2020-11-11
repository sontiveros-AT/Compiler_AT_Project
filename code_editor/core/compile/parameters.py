PYTHON39_PATH = 'language_binaries\python\Python39-32\python.exe'



class Parameters:
    def __init__(self):
        self.__path_language = ''
        self.__file = ''
        self.__version = ''

    def get_language(self):
        return self.__path_language

    def set_language(self, language):
        if language == 'python':
            self.__path_language = PYTHON39_PATH

    def get_file(self):
        return self.__file

    def set_file(self, file):
        self.__file = file
