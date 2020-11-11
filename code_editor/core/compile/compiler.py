import os


class Compiler:
    def __init__(self):
        self.__path_language = ''
        self.__file = ''

    def execute_python(self):
        os.system('python client_files/client_file.py')