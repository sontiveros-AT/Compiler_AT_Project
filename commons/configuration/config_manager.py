#
# @config_manager.py Copyright (c) 2020 Jalasoft.
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

from configparser import ConfigParser

from jala_compiler.settings import BASE_DIR


class ConfigManager:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if ConfigManager.__instance is None:
            ConfigManager.__instance = object.__new__(cls)
            ConfigManager.set_configuration(ConfigManager.__instance)
        return ConfigManager.__instance

    def set_configuration(self):
        self.config_object = ConfigParser()
        self.config_object.read(BASE_DIR / 'config/config.properties')
        self.config_path_compiler = self.config_object['path_compiler']
        self.config_file_template = self.config_object['file_templates']
        self.config_data_base = self.config_object['data_base_config']

    def __init__(self):
        pass

    def get_path_compiler(self, key):
        return self.config_path_compiler[key]

    def get_file_template(self, key):
        return self.config_file_template[key]

    def get_data_base_config(self, key):
        return self.config_data_base[key]
