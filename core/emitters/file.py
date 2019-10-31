from core.model.emitter import ABCEmitter


class FileEmitter(ABCEmitter):
    def __init__(self, path):
        self.path = path

    def emit(self, blob):
        try:
            with open(self.path, 'a') as f:
                f.write(str(blob))
        except Exception as e:
            raise Exception('Could not write to {}'.format(self.path)) from e
