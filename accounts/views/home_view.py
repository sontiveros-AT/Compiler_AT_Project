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
from code_editor.orm_queries.orm_language import OrmLanguage


class HomeView(TemplateView):
    template_name = 'accounts/home.html'

    def get(self, request):
        args = {'username': request.user.username}

        # if OrmLanguage.count_all_language() == 0:
        #     print('No existe nada de nada ')
        #     OrmLanguage.create_new_language('java', '13.0.2', '.java')
        #     OrmLanguage.create_new_language('python', '3.9', '.py')
        #     OrmLanguage.create_new_language('javascript', '14.15.1', '.js')
        #     OrmLanguage.create_new_language('python', '2.7', '.py')
        #     OrmLanguage.create_new_language('php', '7.4.11', '.php')

        return render(request, self.template_name, args)
