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

from django.views.generic import TemplateView
from django.shortcuts import render
from commons.file_manager import FileManager
from django.http import JsonResponse


# class file edit view
class ProjectEditView(TemplateView):
    template_name = 'code_editor/edit.html'

    # get Project
    def get(self, request, id=None, *args, **kwargs):

        return render(request, self.template_name)

    # Create file in project
    def post(self, request, id=None, *args, **kwargs):
        """project_id, file_name, file_path -> post new file in project"""
        project_id = id
        file_name = request.POST['fileName']
        file_path = request.POST['filePath']

        file_manager = FileManager()
        file_manager.create_file(project_id, file_name, file_path)

        return JsonResponse({"response": "file created"})
