from core.model.blob import Blob
from core.model.reader import ABCReader


class RawInputReader(ABCReader):
    def __init__(self, raw_input):
        self.raw_input = raw_input

    def read(self):
        lines = self.raw_input.split('\n')
        name = "Console Input"
        return Blob(name, lines)
