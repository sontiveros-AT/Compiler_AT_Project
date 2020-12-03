#
# @projects_list_view.py Copyright (c) 2020 Jalasoft.
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
# Author: Juan Sebastián Ontiveros Gonzales
# Version: 1.0
#

from django.views.generic import TemplateView
from django.shortcuts import render
from code_editor.orm_queries.orm_project import OrmProject
from accounts.orm_queries.orm_user import OrmUser


# class for project/all endpoint
class ProjectsListView(TemplateView):
    template_name = 'code_editor/projects_list.html'

    # main view list all projects of a logged user
    def get(self, request, *args, **kwargs):
        """user_id -> get all projects"""
        user = OrmUser.get_user(request.user.id)
        projects = OrmProject.get_all_projects(user)
        project_id_name = []
        for project in projects:
            project_id_name.append((project.id, project.name))

        args = {}
        if projects.count() > 0:
            args = {'projects': project_id_name}
        else:
            args = {'message': 'You have no projects.'}

        return render(request, self.template_name, args)
