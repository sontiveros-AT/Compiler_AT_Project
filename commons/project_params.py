#
# @project_params.py Copyright (c) 2020 Jalasoft.
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

from pathlib import Path
from code_editor.orm_queries.orm_language import OrmLanguage
from code_editor.orm_queries.orm_project import OrmProject
from commons.configuration.config_templates import ConfigTemplates


class ProjectParameters():

    def __init__(self, project_id):
        self.project = OrmProject.get_project(project_id)
        self.language = self.project.language
        self.language_name = self.language.name.lower()

    def get_main_file_name(self):
        file_name = ''

        if self.language_name == 'java':
            file_name = 'Main'
        else:
            file_name = 'main'

        return f'{file_name}{self.language.extension}'

    def get_template_code(self, file):
        template_code = ''

        if self.language_name == 'python':
            if self.language.version[0] == '2':
                template_code = ConfigTemplates.get_python27_template()
            if self.language.version[0] == '3':
                template_code = ConfigTemplates.get_python39_template()

        if self.language_name == 'java':
            template_code = self.get_java_class_template(file)

        if self.language_name == 'javascript':
            template_code = ConfigTemplates.get_javascript_template()

        if self.language_name == 'php':
            template_code = ConfigTemplates.get_php_template()

        return template_code

    def get_main_path(self):
        file_path = Path()

        if self.language_name == 'java':
            file_path = Path('src/com')

        return file_path

    def get_file_name_with_ext(self, file_name):
        if self.language.name == 'java':
            file_name = file_name[0].upper() + file_name[1:]

        extension = '.' + str(file_name).split('.')[-1]

        if extension == self.language.extension:
            return file_name

        return file_name + self.language.extension

    def get_java_packages_route(self, path):
        parent = path.parent.as_posix()
        src_index = str(parent).find('src')
        packages = parent[src_index + 4:].replace('/', '.')
        return packages

    def get_java_class_template(self, file):
        file_path = Path(file.path)
        if file.is_main:
            template = '''package com;

public class Main {
    public static void main(String[] args){
        System.out.println("Hello world!");
    }
}'''
        else:
            template = '''package {};

public class {} {{
    
}}'''.format(self.get_java_packages_route(file_path), file_path.stem)
        return template
