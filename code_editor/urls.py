#
# @urls.py Copyright (c) 2020 Jalasoft.
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
from code_editor.views.file_edit_view import FileEditView
from code_editor.views.project_edit_view import ProjectEditView
from code_editor.views.project_view import ProjectView
from code_editor.views.projects_list_view import ProjectsListView


urlpatterns = [
    path('file/<int:id>', FileEditView.as_view(), name='file-view'),
    path('project/', ProjectView.as_view(), name='project-view'),
    path('project/<int:id>', ProjectEditView.as_view(), name='project-edit-view'),
    path('project/all', ProjectsListView.as_view(), name='project-list-view'),
]
