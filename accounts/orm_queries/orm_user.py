#
# @orm_user.py Copyright (c) 2020 Jalasoft.
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

from django.contrib.auth.models import User
from accounts.models import UserProfile

# OrmUser Class provides the different queries to the DB related with Users


class OrmUser:
    # Returns a User Object with the user(from auth_user table)
    @staticmethod
    def get_user_dir(user_id):
        return OrmUser.get_user(user_id).user_dir

    @staticmethod
    def get_user(user_id):
        user = User.objects.get(id=user_id)
        return UserProfile.objects.get(user=user)
