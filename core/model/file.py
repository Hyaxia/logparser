import errno
import os
import sys


class Path(str):
    def __init__(self, pathname=''):
        if not self._pathname_valid(pathname):
            raise Exception('Path {} is not valid!'.format(pathname))
        if pathname.endswith('\\'):
            pathname = pathname[:-1]
        str.__init__(pathname)

    def _pathname_valid(self, pathname):
        ERROR_INVALID_NAME = 123

        try:
            if not isinstance(pathname, str) or not pathname:
                return False
            _, pathname = os.path.splitdrive(pathname)
            root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
                if sys.platform == 'win32' else os.path.sep
            assert os.path.isdir(root_dirname)
            root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep
            for pathname_part in pathname.split(os.path.sep):
                try:
                    os.lstat(root_dirname + pathname_part)
                except OSError as exc:
                    if hasattr(exc, 'winerror'):
                        if exc.winerror == ERROR_INVALID_NAME:
                            return False
                    elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                        return False
        except TypeError as exc:
            return False
        else:
            return True


