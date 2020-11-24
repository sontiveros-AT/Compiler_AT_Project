#
# @settings.py Copyright (c) 2020 Jalasoft.
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

from django.conf import settings


# PATH settings for Java and Python

PYTHON39_PATH = settings.BASE_DIR / 'third_parties/python/Python39-32/python.exe'
JAVA13_PATH = settings.BASE_DIR / 'third_parties/java/jdk-13.0.2/bin'
JAVA_PROJECTS = settings.BASE_DIR / 'media/java'
PYTHON_PROJECTS = settings.BASE_DIR / 'media/python'
