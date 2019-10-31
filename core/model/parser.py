from abc import abstractmethod, ABC


class ABCParser(ABC):
    @abstractmethod
    def parse(self, lines):
        pass

