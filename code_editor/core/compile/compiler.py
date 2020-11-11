import subprocess


class Compiler:
    def __init__(self, params):
        self.__path_language = params.get_language()
        self.__file = params.get_file()

    def execute(self):
        output = subprocess.run([self.__path_language, self.__file], capture_output=True, text=True)
        print('OUTPUT: ', output.stdout)
        print('RETURN CODE: ', output.returncode)
        if output.returncode != 0:
            print(output.stderr)

        # WORKING IN THE ASYNCHRONOUS PROCESS OF GETTING INPUTS AND OUTPUTS
        # p = subprocess.Popen([self.__path_language, self.__file], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        #                      text=True)
        # print("wait output:", p.communicate()[0])
        # print("wait output:", p.wait())

    def execute_java(self):
        pass
