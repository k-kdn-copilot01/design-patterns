"""
Concrete Creator implementations
"""
from creator import Creator
from product import Product
from concrete_products import ConcreteProductA, ConcreteProductB


class ConcreteCreatorA(Creator):
    """
    ConcreteCreatorA - overrides the factory method to return ConcreteProductA
    """
    
    def factory_method(self) -> Product:
        """
        Factory method implementation that creates ConcreteProductA
        
        Returns:
            Product: ConcreteProductA instance
        """
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    """
    ConcreteCreatorB - overrides the factory method to return ConcreteProductB
    """
    
    def factory_method(self) -> Product:
        """
        Factory method implementation that creates ConcreteProductB
        
        Returns:
            Product: ConcreteProductB instance
        """
        return ConcreteProductB()
