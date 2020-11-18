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

import json
from django.http import HttpResponse
from django.views.generic import View


class ProjectView(View):

    def get(self, request, *args, **kwargs):
        response_data = {
            'id': 4,
            'name': 'Test Response',
            'roles': ['Admin', 'User']
        }

        return HttpResponse(json.dumps(response_data), content_type="application/json")
