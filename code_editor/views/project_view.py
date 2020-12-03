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

from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from code_editor.forms import ProjectForm
from commons.file_manager import FileManager


# class for project endpoints
class ProjectView(TemplateView):
    template_name = 'code_editor/new_project.html'

    # main view to create a project
    def get(self, request, *args, **kwargs):
        form = ProjectForm()

        return render(request, self.template_name, {"form": form})

    # endpoint to create a new project for a user
    def post(self, request, *args, **kwargs):
        """project_id, project_name, description, language_id, user -> post new project for a user"""
        project_name = request.POST['project_name']
        description = request.POST['description']
        language_id = int(request.POST['language'])
        user = request.user

        project = FileManager.create_project(
            project_name, description, language_id, user.id)

        if project:
            return redirect('/api/v1/project/{}'.format(project.id))

        render_args = {
            "message": f'The project "{project_name}" already exists!',
            "form": ProjectForm()
        }

        return render(request, self.template_name, render_args)
