#
# @file_edit_view.py Copyright (c) 2020 Jalasoft.
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

import json
from django.views.generic import TemplateView
from django.shortcuts import render
from .file_manager import FileManager
from code_editor.forms import FileForm
from code_editor.core.executor_facade import CompilerFactory
from code_editor.orm_queries.orm_project import OrmProject
from code_editor.orm_queries.orm_file import OrmFile
from django.http import JsonResponse


# class file edit view
class ProjectEditView(TemplateView):
    template_name = 'code_editor/edit.html'
    template_success = 'code_editor/success.html'

    # get file by id
    def get(self, request, id=None, *args, **kwargs):

        # language = OrmProject.get_language_project(id)
        # project = OrmProject.get_project(id)
        #
        # file = OrmProject.get_main_file(id)
        # open_file = FileManager()
        # program = open_file.load_file(file)

        return render(request, self.template_name)

    def post(self, request, id=None, *args, **kwargs):
        language = OrmProject.get_language_project(id)
        project = OrmProject.get_project(id)
        file_name = request.POST['fileName']

        print(language, file_name, project)
        #
        # file = OrmProject.get_main_file(id)
        file_manager = FileManager()
        file_manager.create_file(file_name, id)

        return render(request, self.template_name)

    # def dispatch(self, *args, **kwargs):
    #     method = self.request.POST.get('_method', '').lower()
    #     if method == 'put':
    #         return self.put(*args, **kwargs)
    #     if method == 'delete':
    #         return self.delete(*args, **kwargs)
    #     return super(ProjectEditView, self).dispatch(*args, **kwargs)
    #
    # # update file
    # def put(self, request, *args, **kwargs):
    #     project_id = self.kwargs.get('id')
    #     # data = json.loads(request.body)
    #     # program = data['program']
    #     program = request.POST['program']
    #
    #     # search file in database
    #     file = OrmProject.get_main_file(project_id)
    #
    #     # write program in main file
    #     open_file = FileManager()
    #     open_file.update_file(file, program)
    #
    #     # write updated program
    #     # my_form = FileForm({'program': program})
    #
    #     # get project by id
    #     project = OrmProject.get_project(project_id)
    #
    #     # compile project
    #     comp = CompilerFactory()
    #     compiler = comp.create_compiler(project.language.language_name)
    #     compiler.set_project(project)
    #     output = compiler.run()
    #     # return render(request, self.template_name, {"form": my_form, 'output': output})
    #     # return render(request, self.template_name, {'output': output})
    #     return JsonResponse({"output": output})
    #
    # # delete file
    # def delete(self, request, *args, **kwargs):
    #     id_file = self.kwargs.get('id')
    #     # find file
    #     search_file = OrmFile.get_file(id_file)
    #     print(search_file)
    #     # file = OrmFile.delete_file(id_file)
    #
    #     # remove local storage
    #     # remove = FileManager()
    #     # remove.remove_file(file)
    #
    #     output = 'main file removed'
    #     return render(request, self.template_success, {'output': output})
