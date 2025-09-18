"""
Concrete Product implementations
"""
from product import Product


class ConcreteProductA(Product):
    """
    ConcreteProductA - implements the Product interface
    """
    
    def operation(self) -> str:
        """
        Implement the operation for Product A
        
        Returns:
            str: Description of Product A's operation
        """
        return "Result of ConcreteProductA operation"


class ConcreteProductB(Product):
    """
    ConcreteProductB - implements the Product interface
    """
    
    def operation(self) -> str:
        """
        Implement the operation for Product B
        
        Returns:
            str: Description of Product B's operation
        """
        return "Result of ConcreteProductB operation"
