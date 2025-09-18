"""
Concrete Products for Factory Method pattern.

This module contains concrete implementations of the Product interface.
Each concrete product provides a specific implementation of the product
interface defined in the Product abstract class.
"""

from product import Product


class ConcreteProductA(Product):
    """
    Concrete implementation of Product A.
    
    This class represents a specific type of product that can be created
    by the factory method pattern.
    """
    
    def operation(self) -> str:
        """
        Perform the specific operation for Product A.
        
        Returns:
            str: Result of Product A's operation.
        """
        return "ConcreteProductA: Performing operation A"
    
    def get_info(self) -> str:
        """
        Get information about Product A.
        
        Returns:
            str: Information about Product A.
        """
        return "Product A - Type: Concrete, Category: A"


class ConcreteProductB(Product):
    """
    Concrete implementation of Product B.
    
    This class represents another specific type of product that can be created
    by the factory method pattern.
    """
    
    def operation(self) -> str:
        """
        Perform the specific operation for Product B.
        
        Returns:
            str: Result of Product B's operation.
        """
        return "ConcreteProductB: Performing operation B"
    
    def get_info(self) -> str:
        """
        Get information about Product B.
        
        Returns:
            str: Information about Product B.
        """
        return "Product B - Type: Concrete, Category: B"
