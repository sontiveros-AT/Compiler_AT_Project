#
# @config_template.py Copyright (c) 2020 Jalasoft.
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
# Author: Alvaro Cruz
# Version: 1.0
#

from commons.configuration.config_manager import ConfigManager


class ConfigTemplates:

    @staticmethod
    def get_python39_template():
        con = ConfigManager()
        return con.get_file_template('python39_template')

    @staticmethod
    def get_python27_template():
        con = ConfigManager()
        return con.get_file_template('python27_template')

    @staticmethod
    def get_java_template():
        con = ConfigManager()
        total = ''
        st = con.get_file_template('java13_template')
        list_value = list(st.split('*'))
        total += list_value[0]
        total += "\n\n"
        total += list_value[1]
        total += "\n    "
        total += list_value[2]
        total += "\n        "
        total += list_value[3]
        total += "\n    "
        total += list_value[4]
        total += "\n"
        total += list_value[5]
        return total

    @staticmethod
    def get_javascript_template():
        con = ConfigManager()
        return con.get_file_template('javascript14_template')

    @staticmethod
    def get_php_template():
        con = ConfigManager()
        return con.get_file_template('php7_template')
