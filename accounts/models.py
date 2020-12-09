#
# @models.py Copyright (c) 2020 Jalasoft.
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

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
import hashlib

# UserProfile class extends default django table auth_user


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_dir = models.CharField(max_length=150, default='')

    class Meta:
        db_table = 'user'


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        user_hash = hashlib.md5()
        user_hash.update(user.email.encode('utf-8'))

        user_profile = UserProfile.objects.create(
            user=user,
            user_dir=user_hash.hexdigest()
        )


post_save.connect(create_profile, sender=User)
