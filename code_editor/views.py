
from django.views.generic import TemplateView
from django.shortcuts import render
from Core.compile import Compiler
from Core.compile.parameters import Parameters


class CodeEditorView(TemplateView):
    template_name = 'code_editor/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # establish file and language for params
        params = Parameters()
        params.set_language('python')
        params.set_file(r'../media/python/client_files/client_file.py')

        # execute file
        program = Compiler(params)
        output = program.execute()
        return render(request, self.template_name, {'output': output})
