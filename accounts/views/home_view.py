#
# @home.py Copyright (c) 2020 Jalasoft.
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

from django.shortcuts import render
from django.views.generic import TemplateView


# HomeView class manages get requests for displaying Home page view
class HomeView(TemplateView):
    template_name = 'accounts/home.html'

    def get(self, request):
        args = {'username': request.user.username}
        return render(request, self.template_name, args)
