#
# @file_manager.py Copyright (c) 2020 Jalasoft.
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
# Author: Andres Cox
# Version: 1.0

import os
from pathlib import Path


# class file manager to modify local files
class FileManager:

    # create a file in the media directory based in the language
    def create_file(self, language, project_name, program):
        if language == 'python':
            language = 'python'
            extension = 'py'
            filepath = Path.cwd().joinpath('media/{}/'.format(language, project_name))
            os.mkdir(filepath / project_name)
            file = open(filepath / project_name / 'main.{}'.format(extension), "w")
            file.write(program)
            file.close()
        if language == 'java':
            language = 'java'
            extension = 'java'
            filepath = Path.cwd().joinpath('media/{}/'.format(language, project_name))
            os.makedirs(filepath / project_name / "src/com/",  exist_ok=True)
            file = open(filepath / project_name / 'src/com/Main.{}'.format(extension), "w")
            file.write(program)
            file.close()

    # returns the content of the file targeted
    def load_file(self, filepath):
        file = open(Path.cwd().joinpath(filepath[1:]), "r")
        program = file.read()
        file.close()
        return program

    # overwrite the targeted file with new text
    def update_file(self, filepath, program):
        print("file updated: ", filepath)
        file = open(Path.cwd().joinpath(filepath[1:]), "w")
        program = file.write(program)
        file.close()

    # remove the targeted file
    def remove_file(self, filepath):
        file_to_rem = Path.cwd().joinpath(filepath[1:])
        file_to_rem.unlink()

