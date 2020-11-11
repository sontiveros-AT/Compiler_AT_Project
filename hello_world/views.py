from django.views.generic import TemplateView
from django.shortcuts import render
from hello_world.forms import HelloWorldForm


class HelloWorldView(TemplateView):
    template_name = 'hello_world/index.html'

    def get(self, request):
        form = HelloWorldForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HelloWorldForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
        args = {'form': form, 'first_name': first_name, 'last_name': last_name}

        return render(request, self.template_name, args)

