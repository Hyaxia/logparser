from os.path import basename, getmtime
from datetime import datetime

from core.model.blob import Blob
from core.model.reader import ABCReader


class FileReader(ABCReader):
    def __init__(self, path):
        self.path = path

    def _read_file_content(self):
        try:
            with open(self.path, 'r') as f:
                lines = f.readlines()
                return lines
        except Exception as e:
            raise Exception('Could not read file {}'.format(self.path)) from e

    def _get_name_from_path(self):
        try:
            return basename(self.path)
        except Exception as e:
            raise Exception('Could not get name of file from path {}'.format(self.path)) from e

    def _get_modified_time(self):
        try:
            last_modified_timestamp = getmtime(self.path)
            return datetime.fromtimestamp(last_modified_timestamp).strftime('%d-%m-%Y %H:%M:%S')
        except Exception as e:
            raise Exception('Could not get last modified time of {}'.format(self.path)) from e

    def read(self):
        lines = self._read_file_content()
        name = self._get_name_from_path()
        last_modified = self._get_modified_time()
        return [Blob(name, lines, info={"last_modified": last_modified})]



