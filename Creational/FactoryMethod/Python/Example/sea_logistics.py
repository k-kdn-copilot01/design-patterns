from logistics import Logistics
from ship import Ship

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()
