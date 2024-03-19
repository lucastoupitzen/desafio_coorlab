from abc import ABC, abstractmethod
from ..models.transport import Transport

class FindConfortInterface(ABC):

    @abstractmethod
    def find_confort(self, city: str) -> Transport | None: pass
    