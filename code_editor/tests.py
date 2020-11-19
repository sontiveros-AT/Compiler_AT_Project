from jala_compiler.wsgi import *
from code_editor.orm_queries.orm_file import OrmFile
from code_editor.orm_queries.orm_language import OrmLanguage
from code_editor.orm_queries.orm_project import OrmProject
from code_editor.models.model_language import Language
from code_editor.models.model_project import Project
from code_editor.models.model_file import File
from datetime import datetime

# Create your tests here.

# TO PUT SOME DATA IN THE DATA BASE

# OrmLanguage.create_new_language('java', '.java')
# OrmLanguage.create_new_language('python', '.py')

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

