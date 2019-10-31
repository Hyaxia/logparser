from os import listdir
from os.path import isfile, join

from core.model.reader import ABCMultiReader
from core.readers.file import FileReader


class FolderReader(ABCMultiReader):
    def __init__(self, path):
        self.path = path

    def _get_file_paths_from_folder(self):
        try:
            files = []
            for name in listdir(self.path):
                full_path = join(self.path, name)
                if isfile(full_path):
                    files.append(full_path)
            return files
        except Exception as e:
            raise Exception('Could not get file paths from {}'.format(self.path)) from e

    def read(self):
        file_paths = self._get_file_paths_from_folder()
        return [FileReader(file_path).read() for file_path in file_paths]
