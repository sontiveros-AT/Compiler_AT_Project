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
from code_editor.orm_queries.orm_project import OrmProject
from code_editor.orm_queries.orm_language import OrmLanguage
from accounts.orm_queries.orm_user import OrmUser
from .file_manager import FileManager


def project_names(user):
    proj_names = []
    for project in OrmProject.get_all_projects(user):
        proj_names.append(project.project_name)

    return proj_names

# class for project endpoints


class ProjectView(TemplateView):
    template_name = 'code_editor/new_project.html'

    # main view to create a project
    def get(self, request, *args, **kwargs):
        my_form = ProjectForm()

        return render(request, self.template_name, {"form": my_form})

    # endpoint to create a new project
    def post(self, request, *args, **kwargs):
        project_name = request.POST['project_name']
        description = request.POST['description']
        language_id = request.POST['language']
        user = OrmUser.get_user(request.user)

        render_args = {}
        if project_name in project_names(user):
            render_args = {
                "message": f'The project "{project_name}" already exists!', "form": ProjectForm()}
            return render(request, self.template_name, render_args)

        user_dir = OrmUser.get_user_dir(request.user)
        language = OrmLanguage.get_language(language_id)
        language_name = language.language_name
        language_version = language.language_version
        project_path = f'media/{user_dir}/{language_name}/{language_version}/{project_name}'

        # create project in the database and sends the id
        #project = OrmProject.create_project(project_name, description, project_path, language_name, user)
        project = OrmProject.create_project(project_name, description, project_path, language, user)
        project_id = project.id_project

        # creates file and adds it to the database
        file = FileManager()
        file_name = ''
        if language_name == 'python':
            file_name = 'main'
        elif language_name == 'java':
            file_name = 'Main'
        elif language_name == 'javascript':
            file_name = 'main'
        main_file_path = file.create_file(file_name, project_id)
        OrmProject.update_main_file(project_id, main_file_path)

        return redirect('/api/v1/project/{}'.format(project_id))
