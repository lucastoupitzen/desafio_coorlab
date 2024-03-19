import json
import os
from typing import List
from ....data.interfaces.transport_repo import TransportRepoInterface
from ....domain.models.transport import Transport

class TransportRepo(TransportRepoInterface):

    def _read_json(self):
        data_path = os.path.join(os.pardir, 'data', 'data.json')
        with open(data_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data.get('transport', [])
    
    def read_transports_by_city(self, city):
        transports = self._read_json()
        response = [transport for transport in transports if transport['city'] == city]
        if response.len() == 0:
            raise Exception(f"No transport found for the city {city}!")
        
        return response

    def select_transports_by_city(self, city: str) -> List[Transport] | None:
        
        try:
            raw_response = self.read_transports_by_city(city)
            response : List[Transport] = []
            for resp in raw_response:
                response.append(Transport(
                    id = int(resp.id),
                    name = str(resp.name),
                    price_confort = str(resp.price_confort),
                    price_econ = str(resp.price_econ),
                    city = str(resp.city),
                    duration = str(resp.duration),
                    seat = str(resp.seat),
                    bed = str(resp.bed)
                ))
            return response
        
        except:
            return None
