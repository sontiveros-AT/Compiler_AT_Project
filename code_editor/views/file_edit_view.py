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
from code_editor.forms import FileForm
from commons.file_manager import FileManager
from code_editor.orm_queries.orm_project import OrmProject
from code_editor.orm_queries.orm_file import OrmFile
from django.http import JsonResponse
from django.forms.models import model_to_dict


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

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(FileEditView, self).dispatch(*args, **kwargs)

    # update file endpoint
    def put(self, request, *args, **kwargs):
        """file_id, program -> put program in file"""
        file_id = self.kwargs.get('id')
        program = request.POST['program']

        # search file in database
        file_edit = OrmFile.get_file(file_id)

        # update file
        FileManager.update_file(file_edit.id, program)

        return JsonResponse({"response": "file saved"})

    # delete file endpoint
    def delete(self, request, *args, **kwargs):
        """file_id -> remove file"""
        file_id = self.kwargs.get('id')

        # remove local storage
        remove = FileManager()
        remove.remove_file(file_id)

        return JsonResponse({"response": "file removed"})
