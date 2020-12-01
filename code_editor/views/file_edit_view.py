#
# @file_view.py Copyright (c) 2020 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 subsuelo Edif. La Unión, Av. Gral. Inofuentes, Calacoto, La Paz, Bolivia
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the termns of the license agreement you entered into
# with Jalasoft.
#
# Author: Andres Cox
# Version: 1.0

from django.views.generic import TemplateView
from django.shortcuts import render
from code_editor.forms import FileForm
from code_editor.orm_queries.orm_project import OrmProject
from .file_manager import FileManager
from code_editor.orm_queries.orm_project import OrmProject
from code_editor.orm_queries.orm_file import OrmFile

from django.http import JsonResponse
from django.core.serializers import serialize
import json
from rest_framework import serializers
from django.forms.models import model_to_dict
from code_editor.core.executor_facade import CompilerFactory


# class for file endpoints
class FileEditView(TemplateView):
    template_name = 'code_editor/index.html'

    # get file by id and return json program and more info
    def get(self, request, id=None, *args, **kwargs):
        my_form = FileForm()
        project = OrmProject.get_project(id)
        filess = OrmProject.get_all_files(id)
        files = model_to_dict(filess[0])
        language = model_to_dict(OrmProject.get_language_project(id))
        # for file in filess:
        #     files = files.append(model_to_dict(file))
        file = OrmProject.get_main_file(id)
        open_file = FileManager()
        program = open_file.load_file(file)

        return JsonResponse({"project_name": project.project_name,
                             "program": program,
                             "files": files,
                             "language": language})

        # friendship_requests_list = json.dumps(project)
        # return JsonResponse(friendship_requests_list, safe=False)

    # post endpoint for files
    # def post(self, request, *args, **kwargs):
    #     project_name = request.POST['project_name']
    #     description = request.POST['description']
    #     language = request.POST['language']
    #     program = request.POST['program']
    #
    #     # file = FileManager()
    #     # file.create_file(language, project_name, program)
    #
    #     # OrmProject.create_simple_project(project_name, description, language)
    #
    #     return render(request, self.template_name)
    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(FileEditView, self).dispatch(*args, **kwargs)

    def put(self, request, *args, **kwargs):
        file_id = self.kwargs.get('id')
        # data = json.loads(request.body)
        # program = data['program']
        program = request.POST['program']
        project_id = request.POST['project_id']

        # search file in database
        file = OrmProject.get_main_file(project_id)
        file_edit = OrmFile.get_file(file_id)
        file_path = file_edit.file_path + "/" + file_edit.file_name + ".py"

        # write program in main file
        open_file = FileManager()
        open_file.update_file(file_path, program)

        # get project by id
        project = OrmProject.get_project(project_id)

        # compile project
        comp = CompilerFactory()
        compiler = comp.create_compiler(project.language.language_name)
        compiler.set_project(project)
        output = compiler.run()
        return JsonResponse({"output": output})

    def delete(self, request, *args, **kwargs):
        id_file = self.kwargs.get('id')

        # find file
        search_file = OrmFile.get_file(id_file)
        language = OrmFile.get_file_language(id_file)
        file_path = search_file.file_path + "/" + search_file.file_name + language.language_extension

        # remove from database
        OrmFile.delete_file(id_file)

        # remove local storage
        remove = FileManager()
        remove.remove_file(file_path)

        return JsonResponse({"response": "file removed"})
