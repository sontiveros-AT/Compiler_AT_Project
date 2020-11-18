#
# @file_edit_view.py Copyright (c) 2020 Jalasoft.
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
from code_editor.forms import FileForm


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
        id = self.kwargs.get('id')
        # find file
        file_name = 'demo1'
        extension = 'py'
        file = open(settings.BASE_DIR / r'media\python\{}.{}'.format(file_name, extension), "r")
        print(file.read())
        # update file
        my_form = FileForm({'file_name': 'python operations',
                            'description': 'simple basic operations',
                            'program': "print('hello I am from client file')",
                            'language': "java"
                            })
        # replace and save in the database
        file.close()
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