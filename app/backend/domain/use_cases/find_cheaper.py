from abc import ABC, abstractmethod
from ..models.transport import Transport

class FindCheaperInterface(ABC):

    @abstractmethod
    def find_cheaper(self, city: str) -> Transport | None: pass
