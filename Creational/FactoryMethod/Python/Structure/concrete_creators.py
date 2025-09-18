"""
Concrete Creators for Factory Method pattern.

This module contains concrete implementations of the Creator class.
Each concrete creator implements the factory method to return a specific
concrete product.
"""

from creator import Creator
from concrete_products import ConcreteProductA, ConcreteProductB


class ConcreteCreatorA(Creator):
    """
    Concrete creator that creates ConcreteProductA instances.
    
    This class implements the factory method to return ConcreteProductA.
    """
    
    def factory_method(self) -> ConcreteProductA:
        """
        Factory method that creates and returns ConcreteProductA.
        
        Returns:
            ConcreteProductA: A new instance of ConcreteProductA.
        """
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    """
    Concrete creator that creates ConcreteProductB instances.
    
    This class implements the factory method to return ConcreteProductB.
    """
    
    def factory_method(self) -> ConcreteProductB:
        """
        Factory method that creates and returns ConcreteProductB.
        
        Returns:
            ConcreteProductB: A new instance of ConcreteProductB.
        """
        return ConcreteProductB()
