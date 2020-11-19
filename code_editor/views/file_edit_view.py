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

from django.views.generic import View
from django.shortcuts import render
from code_editor.forms import FileForm
from code_editor.orm_queries.orm_project import OrmProject
from .file_manager import FileManager

#class file edit view
class FileEditView(View):
    template_name = 'code_editor/edit.html'
    template_success = 'code_editor/success.html'

    # get file by id
    def get(self, request, id=None, *args, **kwargs):

        project = OrmProject.get_project(id)
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
        print(self.request.POST)
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

        print(request.POST)
        my_form = FileForm({'program': program,
                            'language': language
                            })
        output = 'file updated'
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