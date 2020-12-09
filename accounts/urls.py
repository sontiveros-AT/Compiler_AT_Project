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
# Author: Juan Sebastián Ontiveros Gonzales
# Version: 1.0
#

from django.urls import path
from accounts.views.home_view import HomeView
from accounts.views.user_login_view import UserLoginView
from accounts.views.user_logout_view import UserLogoutView
from accounts.views.user_reg_view import UserRegisterView
from accounts.views.user_profile_view import UserProfileView
from accounts.views.edit_user_profile_view import EditUserProfileView
from accounts.views.change_password_view import ChangePasswordView

# Url partterns that manage account actions
urlpatterns = [
    path('', HomeView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', EditUserProfileView.as_view(), name='edit_profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]
