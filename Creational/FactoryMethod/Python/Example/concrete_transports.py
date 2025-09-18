"""
Concrete Transport implementations for logistics example.

This module contains concrete implementations of the Transport interface
for different transportation methods: Truck and Ship.
"""

from transport import Transport


class Truck(Transport):
    """
    Concrete implementation of Transport using trucks for road logistics.
    
    Trucks are suitable for land-based transportation with moderate capacity
    and good flexibility for various cargo types.
    """
    
    def __init__(self):
        """Initialize truck with default specifications."""
        self.capacity_kg = 25000  # 25 tons
        self.cost_per_km = 2.5    # $2.5 per km
        self.max_distance_km = 1000  # 1000 km range
    
    def deliver(self, cargo: str, destination: str) -> str:
        """
        Deliver cargo by truck to the specified destination.
        
        Args:
            cargo (str): The cargo to be delivered.
            destination (str): The destination address.
            
        Returns:
            str: Delivery confirmation message.
        """
        return f"🚛 Truck delivered '{cargo}' to {destination} via road transport"
    
    def get_capacity(self) -> str:
        """
        Get truck capacity information.
        
        Returns:
            str: Truck capacity information.
        """
        return f"Truck capacity: {self.capacity_kg:,} kg (25 tons)"
    
    def get_cost_per_km(self) -> float:
        """
        Get truck cost per kilometer.
        
        Returns:
            float: Cost per kilometer for truck transport.
        """
        return self.cost_per_km
    
    def get_transport_info(self) -> str:
        """
        Get detailed truck information.
        
        Returns:
            str: Detailed truck transport information.
        """
        return (f"Truck Transport - Capacity: {self.capacity_kg:,} kg, "
                f"Cost: ${self.cost_per_km}/km, Max Distance: {self.max_distance_km} km")


class Ship(Transport):
    """
    Concrete implementation of Transport using ships for sea logistics.
    
    Ships are suitable for sea-based transportation with high capacity
    and cost-effective for long-distance cargo transport.
    """
    
    def __init__(self):
        """Initialize ship with default specifications."""
        self.capacity_kg = 50000000  # 50,000 tons
        self.cost_per_km = 0.1       # $0.1 per km
        self.max_distance_km = 10000  # 10,000 km range
    
    def deliver(self, cargo: str, destination: str) -> str:
        """
        Deliver cargo by ship to the specified destination.
        
        Args:
            cargo (str): The cargo to be delivered.
            destination (str): The destination address.
            
        Returns:
            str: Delivery confirmation message.
        """
        return f"🚢 Ship delivered '{cargo}' to {destination} via sea transport"
    
    def get_capacity(self) -> str:
        """
        Get ship capacity information.
        
        Returns:
            str: Ship capacity information.
        """
        return f"Ship capacity: {self.capacity_kg:,} kg (50,000 tons)"
    
    def get_cost_per_km(self) -> float:
        """
        Get ship cost per kilometer.
        
        Returns:
            float: Cost per kilometer for ship transport.
        """
        return self.cost_per_km
    
    def get_transport_info(self) -> str:
        """
        Get detailed ship information.
        
        Returns:
            str: Detailed ship transport information.
        """
        return (f"Ship Transport - Capacity: {self.capacity_kg:,} kg, "
                f"Cost: ${self.cost_per_km}/km, Max Distance: {self.max_distance_km} km")
