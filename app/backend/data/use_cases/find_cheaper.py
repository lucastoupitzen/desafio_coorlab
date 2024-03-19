from ...domain.use_cases.find_cheaper import FindCheaperInterface
from ...domain.models.transport import Transport
from ...data.interfaces.transport_repo import TransportRepoInterface

class FindCheaper(FindCheaperInterface):

    def __init__(self, transport_repository: TransportRepoInterface) -> None:
        
        self.__transport_repository = transport_repository

    def find_cheaper(self, city: str) -> Transport | None:
        
        transports_city = self.__transport_repository.select_transports_by_city(city)
        
        if transports_city:
            cheapest = min(transports_city, key=lambda x: 
                           float(x.price_econ.replace('R$', '').strip()))
            return cheapest
        
        return None
        