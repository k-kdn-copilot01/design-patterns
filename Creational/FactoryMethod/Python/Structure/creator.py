"""
Creator class - declares the factory method that returns Product objects
"""
from abc import ABC, abstractmethod
from product import Product


class Creator(ABC):
    """
    Abstract Creator class - declares the factory method that returns a Product object
    """
    
    @abstractmethod
    def factory_method(self) -> Product:
        """
        Factory method that concrete creators must implement
        Note: Despite its name, the Creator's primary responsibility is not creating products.
        Usually, it contains some core business logic that relies on Product objects, 
        returned by the factory method.
        
        Returns:
            Product: A concrete product instance
        """
        pass
    
    def some_operation(self) -> str:
        """
        Some operation that uses the product created by the factory method
        Note: The Creator's code does not depend on concrete product classes
        
        Returns:
            str: Result of the operation using the created product
        """
        # Create a product using the factory method
        product = self.factory_method()
        
        # Use the product
        result = f"Creator: Working with {product.operation()}"
        
        return result
