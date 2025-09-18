"""
Concrete Transport implementations - Truck and Ship
"""
from transport import Transport


class Truck(Transport):
    """
    Truck - implements road transport
    """
    
    def deliver(self) -> str:
        """
        Implement road delivery for trucks
        
        Returns:
            str: Description of truck delivery
        """
        return "Delivering by land in a box via truck"
    
    def get_capacity(self) -> str:
        """
        Get truck capacity information
        
        Returns:
            str: Truck capacity details
        """
        return "Truck capacity: 10-30 tons, suitable for medium-distance land transport"


class Ship(Transport):
    """
    Ship - implements sea transport
    """
    
    def deliver(self) -> str:
        """
        Implement sea delivery for ships
        
        Returns:
            str: Description of ship delivery
        """
        return "Delivering by sea in a container via ship"
    
    def get_capacity(self) -> str:
        """
        Get ship capacity information
        
        Returns:
            str: Ship capacity details
        """
        return "Ship capacity: 1000-10000 tons, suitable for long-distance overseas transport"


class Airplane(Transport):
    """
    Airplane - implements air transport
    """
    
    def deliver(self) -> str:
        """
        Implement air delivery for airplanes
        
        Returns:
            str: Description of airplane delivery
        """
        return "Delivering by air in a cargo hold via airplane"
    
    def get_capacity(self) -> str:
        """
        Get airplane capacity information
        
        Returns:
            str: Airplane capacity details
        """
        return "Airplane capacity: 5-50 tons, suitable for fast international delivery"
