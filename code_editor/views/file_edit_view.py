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
# Author: Andres Cox
# Version: 1.0


from django.views.generic import TemplateView
from django.shortcuts import render
from commons.file_manager import FileManager
from code_editor.forms import FileForm
from code_editor.core.executor_facade import CompilerFactory
from code_editor.orm_queries.orm_project import OrmProject
from commons.settings import BASE_DIR


# class file edit view
class FileEditView(TemplateView):
    template_name = 'code_editor/edit.html'
    template_success = 'code_editor/success.html'

    # get file by id
    def get(self, request, id=None, *args, **kwargs):

        language = OrmProject.get_language_project(id)

        # get and load file
        file = OrmProject.get_main_file(id)
        program = FileManager.load_file(file.id)

        my_form = FileForm({'program': program,
                            'language': language.name
                            })

        return render(request, self.template_name, {"form": my_form})

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(FileEditView, self).dispatch(*args, **kwargs)

    # update file
    def put(self, request, *args, **kwargs):
        project_id = self.kwargs.get('id')
        program = request.POST['program']

        # search file in database
        main_file = OrmProject.get_main_file(project_id)

        # write program in main file
        FileManager.update_file(main_file.id, program)

        # write updated program
        my_form = FileForm({'program': program})

        # get project by id
        project = OrmProject.get_project(project_id)

        # compile project
        comp = CompilerFactory()
        compiler = comp.create_compiler(project.language.name)
        compiler.set_file(main_file)

        output = compiler.run()
        return render(request, self.template_name, {"form": my_form, 'output': output})

    # delete file
    def delete(self, request, *args, **kwargs):
        project_id = self.kwargs.get('id')
        # find file
        main_file = OrmProject.get_main_file(project_id)
        # file_path = BASE_DIR / file
        # file_path.unlink()

        # remove local storage
        remove = FileManager()
        remove.remove_file(main_file.id_file)

        # remove from database
        OrmProject.delete_project(project_id)

        output = 'main file removed'
        return render(request, self.template_success, {'output': output})
