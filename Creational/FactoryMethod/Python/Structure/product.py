"""
Product interface - defines the interface for objects the factory method creates
"""
from abc import ABC, abstractmethod


class Product(ABC):
    """
    Abstract Product class - defines the interface that all concrete products must implement
    """
    
    @abstractmethod
    def operation(self) -> str:
        """
        Define an operation that all concrete products must implement
        
        Returns:
            str: Description of the product's operation
        """
        pass
