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

from django.urls import path
from .views import FileView, FileEditView, ProjectView

urlpatterns = [
    path('file/', FileView.as_view(), name='file-view'),
    path('file/<int:id>', FileEditView.as_view(), name='file-edit-view'),
    path('project/', ProjectView.as_view(), name='project-view'),
]
