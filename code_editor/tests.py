from datetime import datetime

from django.test import TestCase

from code_editor.queries_orm import QueriesORM
from jala_compiler.wsgi import *
from code_editor.Models.model_file import File
from code_editor.Models.model_project import Project
from code_editor.Models.model_language import Language

# Create your tests here.

# lang = Language.objects.get(languageName='java')

# f = Project()
# f.projectName = 'Project1'
# f.description = 'This is my first project'
# f.language = lang
# f.save()

# file_name_given = 'main.java'
# id_project_given = 1

# pro = Project.objects.get(projectName='Project1')

# file = File()
# file.nombre = 'student.java'
# file.path = 'media/file_java/Project1/com/'
# file.date = datetime.strptime('16/11/2020', "%d/%m/%Y")
# file.project = pro
# file.save()

# QUERY

file_name_given = 'main.java'
id_project_given = 1

querysql = File.objects.filter(nombre=file_name_given, project=id_project_given).query
print(querysql)
query = File.objects.get(nombre=file_name_given, project=id_project_given)
print(query.path)

orm = QueriesORM();
orm.create_proyect()
