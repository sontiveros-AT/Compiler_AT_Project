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
# Author: Juan Sebastián Ontiveros Gonzales
# Version: 1.0

from django.http import JsonResponse
from django.views.generic import TemplateView
from commons.jsonify_project import jsonify_project


# Class for file endpoints
class ProjectJSONView(TemplateView):
    template_name = 'code_editor/index.html'

    # get endpoint for files
    def get(self, request, id=None, *args, **kwargs):
        project_json = jsonify_project(id)

        return JsonResponse(project_json)
