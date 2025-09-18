"""
Logistics abstract class for Factory Method pattern example.

This module defines the abstract Logistics class that represents different
logistics companies. Each logistics company can create different types
of transport methods through the factory method pattern.
"""

from abc import ABC, abstractmethod
from transport import Transport


class Logistics(ABC):
    """
    Abstract base class for logistics companies.
    
    The Logistics class declares the factory method that returns a Transport object.
    Different logistics companies can implement this method to return different
    types of transport methods (trucks, ships, planes, etc.).
    """
    
    @abstractmethod
    def create_transport(self) -> Transport:
        """
        Abstract factory method that creates a transport method.
        
        Subclasses must implement this method to return a specific transport type.
        
        Returns:
            Transport: A concrete transport instance.
        """
        pass
    
    def plan_delivery(self, cargo: str, destination: str, distance_km: float) -> str:
        """
        Template method that plans a delivery using the factory method.
        
        This method demonstrates how the logistics company can use the factory method
        to create transport and plan deliveries without knowing the specific transport type.
        
        Args:
            cargo (str): The cargo to be delivered.
            destination (str): The destination address.
            distance_km (float): Distance to destination in kilometers.
            
        Returns:
            str: Delivery plan information.
        """
        transport = self.create_transport()
        
        # Calculate delivery cost
        total_cost = distance_km * transport.get_cost_per_km()
        
        # Create delivery plan
        plan = f"""
📋 Delivery Plan:
   Cargo: {cargo}
   Destination: {destination}
   Distance: {distance_km:,} km
   Transport: {transport.get_transport_info()}
   Estimated Cost: ${total_cost:,.2f}
   
   Delivery: {transport.deliver(cargo, destination)}
        """
        
        return plan.strip()
    
    def get_company_info(self) -> str:
        """
        Get information about the logistics company.
        
        Returns:
            str: Company information.
        """
        transport = self.create_transport()
        return f"Logistics Company - Specializes in: {transport.__class__.__name__} transport"
