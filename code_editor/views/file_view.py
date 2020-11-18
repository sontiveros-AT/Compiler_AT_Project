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

from django.views.generic import View
from django.shortcuts import render
from django.conf import settings
from code_editor.forms import FileForm
from code_editor.core.compile.compiler import Compiler
from code_editor.core.compile.parameters import Parameters


class FileView(View):
    template_name = 'code_editor/index.html'

    def get(self, request, *args, **kwargs):
        my_form = FileForm()

        return render(request, self.template_name, {"form": my_form})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        file_name = request.POST['file_name']
        extension = request.POST['language']
        # create file
        file = open(settings.BASE_DIR / r'media\python\{}.{}'.format(file_name, extension), "w")
        file.write(request.POST['program'])
        file.close()

        # save in the database

        # set parameters
        params = Parameters()
        params.set_language('python')
        params.set_file(settings.BASE_DIR / r'media\python\{}.{}'.format(file_name, extension))

        # execute program
        program = Compiler(params)
        output = program.execute()
        return render(request, self.template_name, {'output': output})