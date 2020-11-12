from django.views.generic import TemplateView
from django.shortcuts import render
from code_editor.core.compile.compiler import Compiler
from code_editor.core.compile.parameters import Parameters
from jala_compiler.settings import BASE_DIR


class CodeEditorView(TemplateView):
    template_name = 'code_editor/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        params = Parameters()
        params.set_language('python')
        params.set_file(r'D:\ProgramFiles\python\Compiler_AT_Project\media\python\client_files\client_file.py')

        program = Compiler(params)
        output = program.execute()

        return render(request, self.template_name, {'output': output})
