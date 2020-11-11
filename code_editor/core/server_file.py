from compile.compiler import Compiler
from compile.parameters import Parameters

params = Parameters()
params.set_language('python')
params.set_file('client_files/client_file.py')

program = Compiler(params)
program.execute()
