from code_editor.core.exceptions.exceptions import ExecuteInvalidException, LanguageInvalidException, \
    ParametersInvalidException
from jala_compiler.wsgi import *
from code_editor.orm_queries.orm_file import OrmFile
from code_editor.orm_queries.orm_language import OrmLanguage
from code_editor.orm_queries.orm_project import OrmProject

# from code_editor.models.model_language import Language
from code_editor.models.model_project import Project
# from code_editor.models.model_file import File
# from datetime import datetime

# Create your tests here.

# TO PUT SOME DATA IN THE DATA BASE

# OrmLanguage.create_new_language('java', '13.0.2', '.java')
# OrmLanguage.create_new_language('python', '3.9', '.py')
# OrmLanguage.create_new_language('javascript', '14.15.1', '.js')


# OrmProject.create_project('ProjectJava1', 'This is a Java Project 1', 'java')
# OrmProject.create_project('ProjectPython1', 'This is a Python Project 1', 'python')
# OrmProject.create_project('ProjectJava2', 'This is a Java Project 2', 'java')

# OrmFile.create_file(1, 'main')
# OrmFile.create_file(1, 'fileJava1')
# OrmFile.create_file(1, 'fileJava2')
# OrmFile.create_file(2, 'main_python')
# OrmFile.create_file(2, 'file_python1')
# OrmFile.create_file(3, 'main')
# OrmFile.create_file(3, 'file_java')


# QUERY
# SELECT * FROM file WHERE id_project='1' AND name='main.java'
# file_name_given = 'main'
# id_project_given = 1
# try:
#     querysql = File.objects.filter(file_name='main', project_id=1).query
#     print(querysql)
#     query = File.objects.get(file_name='main', project_id=1)
#     print(query.file_path)
# except Exception as e:
#    print(e)

# from code_editor.orm_queries.orm_project import OrmProject
from code_editor.core.executor_facade import CompilerFactory
# #
# project = OrmProject.get_project(1)
# language = 'python'
# print(project.project_name)
#
# try:
#     comp = CompilerFactory()
#     compiler = comp.create_compiler(language)
#     compiler.set_project(project)
#     print(compiler.run())
# except LanguageInvalidException as e:
#     print(e)
# except ParametersInvalidException as e:
#     print(e)
# except ExecuteInvalidException as e:
#     print(e)
#
# import subprocess
#
# cmd = ["C:/Tests/CompilerProjectUser/Compiler_AT_Project/third_parties/javascript/nodejs14.15.1/node.exe",
# "C:/Users/acruz/Desktop/filejs.js"]
#
# process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# output, errors = process.communicate()
# print(output)

#
# OrmProject.hard_project('ProjectJavascript1', 'This is project js',
#                         'media/808eb9893815d1931afaea1dfe57dfb6/javascript/14.15.1/ProjectJavascript1',
#                         'media/808eb9893815d1931afaea1dfe57dfb6/javascript/14.15.1/ProjectJavascript1/main.js')


# OrmFile.create_file('main', 'media/808eb9893815d1931afaea1dfe57dfb6/javascript/14.15.1/ProjectJavascript1', 10)


project = OrmProject.get_project(10)
language = 'javascript'
print(project.project_name)

comp = CompilerFactory()
compiler = comp.create_compiler(language)
compiler.set_project(project)
print(compiler.run())
