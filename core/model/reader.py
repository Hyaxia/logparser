from typing import List
from abc import abstractmethod, ABC
from core.model.blob import Blob


class ABCReader(ABC):
    @abstractmethod
    def read(self) -> List[Blob]:
        pass
