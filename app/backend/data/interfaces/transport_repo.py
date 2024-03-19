from typing import List
from abc import ABC, abstractmethod
from ...domain.models.transport import Transport


class TransportRepoInterface(ABC):

    @abstractmethod
    def select_transports_by_city(self, city: str) -> List[Transport] | None: pass
    