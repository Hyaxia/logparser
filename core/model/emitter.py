from abc import abstractmethod, ABC


class ABCEmitter(ABC):
    @abstractmethod
    def emit(self, blob):
        pass

