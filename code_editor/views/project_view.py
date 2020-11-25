#
# @project_view.py Copyright (c) 2020 Jalasoft.
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

from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import redirect
from code_editor.forms import ProjectForm
from code_editor.orm_queries.orm_project import OrmProject
from .file_manager import FileManager


# class for project endpoints
class ProjectView(View):
    template_name = 'code_editor/home.html'

    # main view to create a project
    def get(self, request, *args, **kwargs):
        my_form = ProjectForm()

        return render(request, self.template_name, {"form": my_form})

    # endpoint to create a new project
    def post(self, request, *args, **kwargs):
        project_name = request.POST['project_name']
        description = request.POST['description']
        language = request.POST['language']
        program = "hello"

        # creates file
        file = FileManager()
        file.create_file(language, project_name, program)

        # create project in th database and sends the id
        project = OrmProject.create_simple_project(project_name, description, language)
        id = project.id_project
        return redirect('/api/v1/file/{}'.format(id))
