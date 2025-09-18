"""
Logistics classes - abstract and concrete implementations
"""
from abc import ABC, abstractmethod
from transport import Transport
from vehicles import Truck, Ship, Airplane


class Logistics(ABC):
    """
    Abstract Logistics class - declares the factory method for creating transport
    """
    
    @abstractmethod
    def create_transport(self) -> Transport:
        """
        Factory method that concrete logistics must implement
        
        Returns:
            Transport: A concrete transport instance
        """
        pass
    
    def plan_delivery(self) -> str:
        """
        Core business logic that uses the transport created by the factory method
        
        Returns:
            str: Delivery plan details
        """
        # Create transport using the factory method
        transport = self.create_transport()
        
        # Use the transport for delivery planning
        capacity_info = transport.get_capacity()
        delivery_method = transport.deliver()
        
        result = f"Logistics Planning:\n- {capacity_info}\n- {delivery_method}"
        return result


class RoadLogistics(Logistics):
    """
    RoadLogistics - creates trucks for land transport
    """
    
    def create_transport(self) -> Transport:
        """
        Factory method implementation that creates trucks
        
        Returns:
            Transport: Truck instance
        """
        return Truck()


class SeaLogistics(Logistics):
    """
    SeaLogistics - creates ships for sea transport
    """
    
    def create_transport(self) -> Transport:
        """
        Factory method implementation that creates ships
        
        Returns:
            Transport: Ship instance
        """
        return Ship()


class AirLogistics(Logistics):
    """
    AirLogistics - creates airplanes for air transport
    """
    
    def create_transport(self) -> Transport:
        """
        Factory method implementation that creates airplanes
        
        Returns:
            Transport: Airplane instance
        """
        return Airplane()
