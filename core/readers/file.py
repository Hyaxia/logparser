from os import listdir
from os.path import isfile, join, basename, getmtime
from datetime import datetime

from core.model.blob import Blob


def _get_name_from_path(path):
    try:
        return basename(path)
    except Exception as e:
        raise Exception('Could not get name of file from path {}'.format(path)) from e


def _get_file_paths_from_folder(folder_path):
    try:
        files = []
        for name in listdir(folder_path):
            full_path = join(folder_path, name)
            if isfile(full_path):
                files.append(full_path)
        return files
    except Exception as e:
        raise Exception('Could not get file paths from {}'.format(folder_path)) from e


def _get_file_name_from_paths(file_paths):
    return [_get_name_from_path(file_path) for file_path in file_paths]


def _get_modified_time(path):
    try:
        last_modified_timestamp = getmtime(path)
        return datetime.fromtimestamp(last_modified_timestamp).strftime('%d-%m-%Y %H:%M:%S')
    except Exception as e:
        raise Exception('Could not get last modified time of {}'.format(path)) from e


def _read_file_content(path):
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
            return lines
    except Exception as e:
        raise Exception('Could not read file {}'.format(path)) from e


def file_reader(path):
    lines = _read_file_content(path)
    name = _get_name_from_path(path)
    last_modified = _get_modified_time(path)
    return Blob(name, lines, info={"last_modified": last_modified})


def folder_reader(folder_path):
    file_paths = _get_file_paths_from_folder(folder_path)
    return [file_reader(file_path) for file_path in file_paths]





