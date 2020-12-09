from pathlib import Path
from code_editor.orm_queries.orm_project import OrmProject
from commons.file_manager import FileManager


def get_child(tree, child_name):
    for child in tree:
        if child['name'] == child_name:
            return child

    return {}


def exists_dir(tree, dir_name):
    for child in tree:
        if child['name'] == dir_name:
            return True

    return False


def walk(file, root_path, tree):
    file_path = file_path_from_root(file.path, root_path)
    file_parents = Path(file_path).parts
    if len(file_parents) == 1:
        tree.append({
            'name': file.name,
            'fileId': file.id,
            'program': FileManager.load_file(file.id)
        })
    elif len(file_parents) > 1:
        dir_name = file_parents[0]
        if not exists_dir(tree, dir_name):
            tree.append({
                'name': dir_name,
                'open': True,
                'isParent': True,
                'children': []
            })
            sub_tree = tree[-1]
        else:
            sub_tree = get_child(tree, dir_name)

        root_path = root_path + '\\' + dir_name
        walk(file, root_path, sub_tree['children'])


def file_path_from_root(file_path, root):
    return file_path.replace(root + '\\', '')


def jsonify_project(project_id):
    project = OrmProject.get_project(project_id)
    project_files = OrmProject.get_all_files(project_id)

    file_tree = []
    file_tree.append({
        'name': project.name,
        'open': True,
        'isParent': True,
        'children': []
    })

    for file in project_files:
        walk(file, project.path, file_tree[0]['children'])

    json = {
        'projectName': project.name,
        'projectPath': project.path,
        'projectDescription': project.description,
        'projectId': project.id,
        'languageId': project.language.id,
        'languageName': project.language.name,
        'languageExtension': project.language.extension,
        'content': file_tree
    }

    return json
