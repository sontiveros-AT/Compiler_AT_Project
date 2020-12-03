#
# @config_database.py Copyright (c) 2020 Jalasoft.
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


class ConfigurationDatabase:
    @staticmethod
    def get_db_name():
        con = ConfigManager()
        return con.get_data_base_config('db_name')

    @staticmethod
    def get_db_user():
        con = ConfigManager()
        return con.get_data_base_config('db_user')

    @staticmethod
    def get_db_password():
        con = ConfigManager()
        return con.get_data_base_config('db_password')

    @staticmethod
    def get_db_hostname():
        con = ConfigManager()
        return con.get_data_base_config('db_hostname')

    @staticmethod
    def get_db_port():
        con = ConfigManager()
        return con.get_data_base_config('db_port')
