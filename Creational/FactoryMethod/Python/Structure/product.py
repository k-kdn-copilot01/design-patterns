"""
Product interface for Factory Method pattern.

This module defines the abstract Product class that all concrete products
must implement. The Product interface declares the operations that all
concrete products must implement.
"""

from abc import ABC, abstractmethod


class Product(ABC):
    """
    Abstract base class for all products created by the factory method.
    
    This class defines the interface that all concrete products must implement.
    The factory method pattern ensures that the creator class doesn't need to
    know the specific class of the product it creates.
    """
    
    @abstractmethod
    def operation(self) -> str:
        """
        Abstract method that all concrete products must implement.
        
        Returns:
            str: A string representing the result of the product's operation.
        """
        pass
    
    @abstractmethod
    def get_info(self) -> str:
        """
        Abstract method to get information about the product.
        
        Returns:
            str: Information about the product.
        """
        pass
