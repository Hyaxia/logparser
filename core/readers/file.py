from os import listdir
from os.path import isfile, join, basename, getmtime

from core.model.blob import Blob


def _get_name_from_path(path):
    return basename(path)


def _get_file_paths_from_folder(folder_path):
    return [f for f in listdir(folder_path) if isfile(join(folder_path, f))]


def _get_file_name_from_paths(file_paths):
    return [_get_name_from_path(file_path) for file_path in file_paths]


def file_reader(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    name = _get_name_from_path(path)
    last_modified = getmtime(path)
    return Blob(name, lines, info={last_modified: last_modified})


def folder_reader(folder_path):
    file_paths = _get_file_paths_from_folder(folder_path)
    return [file_reader(file_path) for file_path in file_paths]





