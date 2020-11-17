#
# @main.py Copyright (c) 2020 Jalasoft.
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
from pathlib import Path
from .forms import FileForm
from code_editor.core.compile.compiler import Compiler
from code_editor.core.compile.parameters import Parameters

import json
from django.http import HttpResponse


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


class FileEditView(View):
    template_name = 'code_editor/edit.html'
    template_success = 'code_editor/success.html'

    # get file by id
    def get(self, request, id=None, *args, **kwargs):
        # print('program id: ', id)

        # load file
        my_form = FileForm({'file_name': 'python operations',
                            'description': 'simple basic operations',
                            'program': "print('hello I am from client file')",
                            'language': "py"
                            })

        return render(request, self.template_name, {"form": my_form})

    def dispatch(self, *args, **kwargs):
        print(self.request.POST)
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(FileEditView, self).dispatch(*args, **kwargs)

    # update file
    def put(self, request, *args, **kwargs):
        print("Hello, i'm %s!" % self.request.POST.get('_method'))
        id = self.kwargs.get('id')
        # find file

        # update file
        my_form = FileForm({'file_name': 'python operations',
                            'description': 'simple basic operations',
                            'program': "print('hello I am from client file')",
                            'language': "java"
                            })
        # replace and save in the database
        output = 'file updated'
        return render(request, self.template_success, {'output': output})

    # delete file
    def delete(self, request, *args, **kwargs):
        print("Hello, i'm %s!" % self.request.POST.get('_method'))
        id = self.kwargs.get('id')
        print(id)
        # find file
        # remove
        file_name = 'demo1'
        extension = 'py'
        file_to_rem = Path(settings.BASE_DIR / r'media\python\{}.{}'.format(file_name, extension))
        file_to_rem.unlink()

        output = 'user file removed'
        return render(request, self.template_success, {'output': output})


class ProjectView(View):

    def get(self, request, *args, **kwargs):
        response_data = {
            'id': 4,
            'name': 'Test Response',
            'roles': ['Admin', 'User']
        }

        return HttpResponse(json.dumps(response_data), content_type="application/json")
