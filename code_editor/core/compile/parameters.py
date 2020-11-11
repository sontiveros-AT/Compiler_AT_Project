class Parameters:
    def __init__(self):
        self.__path_language = ''
        self.__file = ''

    def get_path_language(self):
        return self.__path_language

    def set_path_language(self, path_language):
        self.__path_language = path_language

    def get_file(self):
        return self.__file

    def set_file(self, file):
        self.__file = file