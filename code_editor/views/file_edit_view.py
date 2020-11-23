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

from pathlib import Path
from django.views.generic import View
from django.shortcuts import render
from code_editor.orm_queries.orm_project import OrmProject
from .file_manager import FileManager
from code_editor.forms import FileForm
from code_editor.core.executor_facade import ExecutorManager


# class file edit view
class FileEditView(View):
    template_name = 'code_editor/edit.html'
    template_success = 'code_editor/success.html'

    # get file by id
    def get(self, request, id=None, *args, **kwargs):

        language = OrmProject.get_language_project(id)

        file = OrmProject.get_main_file_project(id)
        open_file = FileManager()
        program = open_file.load_file(file.file_path)

        # load file
        my_form = FileForm({'program': program,
                            'language': language.language_name
                            })

        return render(request, self.template_name, {"form": my_form})

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(FileEditView, self).dispatch(*args, **kwargs)

    # update file
    def put(self, request, *args, **kwargs):
        id = self.kwargs.get('id')

        language = request.POST['language']
        program = request.POST['program']

        file = OrmProject.get_main_file_project(id)
        open_file = FileManager()
        open_file.update_file(file.file_path, program)

        my_form = FileForm({'program': program,
                            'language': language
                            })

        project = OrmProject.get_project(id)
        project_name = project.project_name
        file_path = Path.cwd().joinpath(file.file_path[1:])

        extension = request.POST['language']

        if extension == "python":
            compiler = ExecutorManager()
            compiler.set_language('python')
            compiler.set_file(file_path)

        if extension == "java":
            compiler = ExecutorManager()
            compiler.set_language('java')
            compiler.set_file(project_name)

        output = compiler.run()

        return render(request, self.template_name, {"form": my_form, 'output': output})

    # delete file
    def delete(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        # find file
        file = OrmProject.get_main_file_project(id)

        # remove local storage
        remove = FileManager()
        remove.remove_file(file.file_path)

        # remove from database
        OrmProject.delete_project(id)

        output = 'main file removed'
        return render(request, self.template_success, {'output': output})
