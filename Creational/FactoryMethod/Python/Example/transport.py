"""
Transport interface for logistics example.

This module defines the abstract Transport class that represents different
types of transportation methods in a logistics system.
"""

from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Abstract base class for all transport methods.
    
    This class defines the interface that all concrete transport methods
    must implement in the logistics system.
    """
    
    @abstractmethod
    def deliver(self, cargo: str, destination: str) -> str:
        """
        Abstract method to deliver cargo to a destination.
        
        Args:
            cargo (str): The cargo to be delivered.
            destination (str): The destination address.
            
        Returns:
            str: Delivery confirmation message.
        """
        pass
    
    @abstractmethod
    def get_capacity(self) -> str:
        """
        Abstract method to get the transport capacity.
        
        Returns:
            str: Information about the transport capacity.
        """
        pass
    
    @abstractmethod
    def get_cost_per_km(self) -> float:
        """
        Abstract method to get the cost per kilometer.
        
        Returns:
            float: Cost per kilometer for this transport method.
        """
        pass
    
    @abstractmethod
    def get_transport_info(self) -> str:
        """
        Abstract method to get detailed transport information.
        
        Returns:
            str: Detailed information about the transport method.
        """
        pass
