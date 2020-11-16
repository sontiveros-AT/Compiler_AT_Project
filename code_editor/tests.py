from datetime import datetime

from django.test import TestCase
from jala_compiler.wsgi import *
from code_editor.models import Languages
from code_editor.models import Projects
from code_editor.models import Files

# Create your tests here.

#lang = Languages.objects.get(languageName='java')

#f = Projects()
#f.projectName = 'Project1'
#f.description = 'This is my first project'
#f.language = lang
#f.save()

#file_name_given = 'main.java'
#id_project_given = 1

#pro = Projects.objects.get(projectName='Project1')

#file = Files()
#file.nombre = 'student.java'
#file.path = 'media/file_java/Project1/com/'
#file.date = datetime.strptime('16/11/2020', "%d/%m/%Y")
#file.project = pro
#file.save()

#QUERY

file_name_given = 'main.java'
id_project_given = 1

query = Files.objects.get(nombre=file_name_given, project = id_project_given)
print(query.path)



