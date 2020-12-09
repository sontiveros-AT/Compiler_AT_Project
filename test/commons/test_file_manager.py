#
# @test_file_manager.py Copyright (c) 2020 Jalasoft.
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

import unittest
from commons.file_manager import FileManager
from code_editor.models.model_project import Project
from code_editor.models.model_file import File
from code_editor.orm_queries.orm_project import OrmProject


# Class TestFileManager to test FileManager class
class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.project_name = 'test_project'
        self.project_description = 'A dummy project for testing FileManager class'
        self.language_id = 1
        self.user_id = 1
        self.project_id = 0

    def tearDown(self):
        if self.project_id > 0:
            OrmProject.delete_project(self.project_id)

# Tests for .is_repeated_project()
# Test when the project is not repeated
    def test_project_not_repeated_is_repeated_project(self):
        is_repeated = FileManager.is_repeated_project(
            self.project_name,
            self.language_id,
            self.user_id)

        self.assertFalse(is_repeated)

# Test when the project already exists
    def test_project_is_repeated_is_repeated_project(self):
        project = FileManager.create_project(
            self.project_name,
            self.project_description,
            self.language_id,
            self.user_id)

        is_repeated = FileManager.is_repeated_project(
            self.project_name,
            self.language_id,
            self.user_id)

        self.assertTrue(is_repeated)

# Test when it receives either empty strings or 0 as language and user id's
    def test_empty_zero_is_repeated_project(self):
        is_repeated = FileManager.is_repeated_project('', 0, 0)

        self.assertFalse(is_repeated)

# Test when it receives either None as strings or NaN as language and user id's
    def test_None_NaN_is_repeated_project(self):
        is_repeated = FileManager.is_repeated_project('', 0, 0)

        self.assertFalse(is_repeated)

# Tests for .create_project() method
# Test with valid data
    def test_valid_create_project(self):
        project = FileManager.create_project(
            self.project_name,
            self.project_description,
            self.language_id,
            self.user_id)

        self.assertIsInstance(project, Project)
        self.assertEqual(project.name, self.project_name)
        self.assertEqual(project.description, self.project_description)
        self.assertEqual(project.language, self.language_id)
        self.assertEqual(project.user, self.user_id)
        self.project_id = project.id

# Test with emtpy strings and zero for ids
    def test_empty_zero_create_project(self):
        project = FileManager.create_project('', '', 0, 0)

        self.assertIsNone(project)

# Test with None for strings and NaN for ids
    def test_None_NaN_create_project(self):
        project = FileManager.create_project(None, None, 'NaN', 'NaN')

        self.assertIsNone(project)

# Tests for .is_repeated_file()
# Test when the file is not repeated
    def test_file_is_not_repeated_is_repeated_file(self):
        project = FileManager.create_project(
            self.project_name,
            self.project_description,
            self.language_id,
            self.user_id)

        file_path = f'media/dummy_file.txt'
        is_repeated = FileManager.is_repeated_file(project.id, file_path)
        self.project_id = project.id

        self.assertFalse(is_repeated)

# Test when the file already exists
    def test_file_is_repeated_is_repeated_file(self):
        project = FileManager.create_project(
            self.project_name,
            self.project_description,
            self.language_id,
            self.user_id)

        file_path = OrmProject.get_main_file(project.id).path
        is_repeated = FileManager.is_repeated_file(project.id, file_path)
        self.project_id = project.id

        self.assertTrue(is_repeated)

# Test when with zero for project id and empty string for file_path
    def test_empty_zero_is_repeated_file(self):
        is_repeated = FileManager.is_repeated_file(0, '')

        self.assertTrue(is_repeated)

# Test with None and NaN
    def test_None_NaN_is_repeated_file(self):
        is_repeated = FileManager.is_repeated_file('NaN', None)

        self.assertFalse(is_repeated)

# Tests for .create_file
# Test with valid data with no path given
    def test_valid_no_path_create_file(self):
        project = FileManager.create_project(
            self.project_name,
            self.project_description,
            self.language_id,
            self.user_id)

        file = FileManager.create_file(project.id, 'file')
        self.project_id = project.id

        self.assertIsInstance(file, File)

# Test with valid data with given path
    def test_valid_with_path_create_file(self):
        project = FileManager.create_project(
            self.project_name,
            self.project_description,
            self.language_id,
            self.user_id)

        file = FileManager.create_file(project.id, 'file', 'folder')
        self.project_id = project.id

        self.assertIsInstance(file, File)

# Test with 0 for project_id and empty strings
    def test_empty_zero_create_file(self):
        file = FileManager.create_file(0, '')

        self.assertIsNone(file)

# Test with NaN for project_id and None strings
    def test_None_NaN_create_file(self):
        file = FileManager.create_file('NaN', None, None)

        self.assertIsNone(file)

# Tests for .load_file()
# Test with valid file id
    def test_valid_load_file(self):
        project = FileManager.create_project(
            self.project_name,
            self.project_description,
            self.language_id,
            self.user_id)

        file_id = OrmProject.get_main_file(project.id).id
        program = FileManager.load_file(file_id)
        self.assertIsNotNone(program)

# Test with invalid file id
    def test_invalid_id_load_file(self):
        program = FileManager.load_file(99999)
        self.assertIsNone(program)


if __name__ == '__main__':
    unittest.main
