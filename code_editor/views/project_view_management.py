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

from django.http import JsonResponse
from django.views.generic import TemplateView
from code_editor.orm_queries.orm_project import OrmProject
from code_editor.core.executor_facade import CompilerFactory


# Class for file endpoints
class ProjectViewManagement(TemplateView):
    template_name = 'code_editor/index.html'

    # endpoint to compile main file of a project
    def get(self, request, id=None, *args, **kwargs):
        """project_id -> output"""
        project_id = self.kwargs.get('id')

        # search file in database
        main_file = OrmProject.get_main_file(project_id)

        # get project by id
        project = OrmProject.get_project(project_id)

        # compile project
        comp = CompilerFactory()
        compiler = comp.create_compiler(project.language.name)
        compiler.set_file(main_file)
        output = compiler.run()
        return JsonResponse({"output": output})
