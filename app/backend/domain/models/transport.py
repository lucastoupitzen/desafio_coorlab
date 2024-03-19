class Transport():

    def __init__(self, id: int, name: str, price_confort: str,
                price_econ: str, city: str, duration: str,
                seat: str, bed: str) -> None:
        
        self.id = id
        self.name = name
        self.price_confort = price_confort
        self.price_econ = price_econ
        self.city = city
        self.duration = duration
        self.seat = seat
        self.bed = bed
