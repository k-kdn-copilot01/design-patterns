"""
Concrete Logistics implementations for Factory Method pattern example.

This module contains concrete implementations of the Logistics class
for different logistics companies: RoadLogistics and SeaLogistics.
"""

from logistics import Logistics
from concrete_transports import Truck, Ship


class RoadLogistics(Logistics):
    """
    Concrete logistics company that specializes in road transportation.
    
    RoadLogistics creates Truck instances for land-based cargo delivery.
    Suitable for domestic deliveries and short to medium distance transport.
    """
    
    def create_transport(self) -> Truck:
        """
        Factory method that creates and returns a Truck instance.
        
        Returns:
            Truck: A new Truck instance for road transportation.
        """
        return Truck()
    
    def get_company_info(self) -> str:
        """
        Get information about RoadLogistics company.
        
        Returns:
            str: RoadLogistics company information.
        """
        return "RoadLogistics - Specializes in: Truck transport for land-based deliveries"


class SeaLogistics(Logistics):
    """
    Concrete logistics company that specializes in sea transportation.
    
    SeaLogistics creates Ship instances for sea-based cargo delivery.
    Suitable for international deliveries and large volume transport.
    """
    
    def create_transport(self) -> Ship:
        """
        Factory method that creates and returns a Ship instance.
        
        Returns:
            Ship: A new Ship instance for sea transportation.
        """
        return Ship()
    
    def get_company_info(self) -> str:
        """
        Get information about SeaLogistics company.
        
        Returns:
            str: SeaLogistics company information.
        """
        return "SeaLogistics - Specializes in: Ship transport for sea-based deliveries"
