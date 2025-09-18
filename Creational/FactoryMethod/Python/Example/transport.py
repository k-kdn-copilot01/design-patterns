"""
Transport interface - defines the interface for transport vehicles
"""
from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Abstract Transport class - defines the interface that all transport vehicles must implement
    """
    
    @abstractmethod
    def deliver(self) -> str:
        """
        Define a delivery method that all transport vehicles must implement
        
        Returns:
            str: Description of how the transport delivers
        """
        pass
    
    @abstractmethod
    def get_capacity(self) -> str:
        """
        Get the capacity information of the transport
        
        Returns:
            str: Capacity description
        """
        pass
