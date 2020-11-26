#
# @user_reg_view.py Copyright (c) 2020 Jalasoft.
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

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from accounts.forms.reg_form import RegistrationForm

# UserRegisterView manages get and post requests for user registration page


class UserRegisterView(TemplateView):

    def get(self, request):
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'registration/reg_form.html', args)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/register')
