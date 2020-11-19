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
from code_editor.forms import FileForm
from code_editor.orm_queries.orm_project import OrmProject
from .file_manager import FileManager


class FileView(View):
    template_name = 'code_editor/index.html'

    def get(self, request, *args, **kwargs):
        my_form = FileForm()

        return render(request, self.template_name, {"form": my_form})

    def post(self, request, *args, **kwargs):
        project_name = request.POST['project_name']
        description = request.POST['description']
        language = request.POST['language']
        program = request.POST['program']

        file = FileManager()
        file.create_file(language, project_name, program)

        OrmProject.create_simple_project(project_name, description, language)

        # set parameters
        # params = Parameters()
        # params.set_language('python')
        # params.set_file(settings.BASE_DIR / r'media\python\{}.{}'.format(file_name, extension))
        #
        # # execute program
        # program = Compiler(params)
        # output = program.execute()
        def post(self, request, *args, **kwargs):
            print(request.POST)
            file_name = request.POST['file_name']
            extension = request.POST['language']

            if extension == "py":
                file_path = settings.BASE_DIR / \
                            f'media/python/{file_name}.{extension}'

                # create file
                file = open(file_path, "w")
                file.write(request.POST['program'])
                file.close()

                # save in the database

                # set parameters
                compiler = ExecutorManager()
                compiler.set_language('python')
                compiler.set_file(file_path)

            if extension == "java":
                # create file
                file_path = settings.BASE_DIR / \
                            f'media/java/{file_name}/src/com/Main.{extension}'
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                with open(file_path, "w") as file:
                    file.write(request.POST['program'])

                # save in the database

                # set parameters
                compiler = ExecutorManager()
                compiler.set_language('java')
                compiler.set_file(file_name)
            # execute program
        output = "this is in development"
        return render(request, self.template_name, {'output': output})