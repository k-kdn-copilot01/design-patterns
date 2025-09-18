"""
Creator abstract class for Factory Method pattern.

This module defines the abstract Creator class that declares the factory method.
The Creator class is responsible for creating products, but it delegates the
actual creation to subclasses through the factory method.
"""

from abc import ABC, abstractmethod
from product import Product


class Creator(ABC):
    """
    Abstract base class for creators in the Factory Method pattern.
    
    The Creator class declares the factory method that returns a Product object.
    The Creator may also define a default implementation of the factory method
    that returns a default concrete product.
    """
    
    @abstractmethod
    def factory_method(self) -> Product:
        """
        Abstract factory method that creates a product.
        
        Subclasses must implement this method to return a specific concrete product.
        
        Returns:
            Product: A concrete product instance.
        """
        pass
    
    def some_operation(self) -> str:
        """
        Template method that uses the factory method.
        
        This method demonstrates how the creator can use the factory method
        without knowing the specific concrete product class.
        
        Returns:
            str: Result of the operation using the created product.
        """
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result
