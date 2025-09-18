from abstract_factory import AbstractFactory
from abstract_products import AbstractProductA, AbstractProductB
from concrete_products import ConcreteProductA1, ConcreteProductA2, ConcreteProductB1, ConcreteProductB2


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factory 1 produces a family of products belonging to the first variant.
    The factory guarantees that resulting products are compatible.
    """
    
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Concrete Factory 2 produces a family of products belonging to the second variant.
    The factory guarantees that resulting products are compatible.
    """
    
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
