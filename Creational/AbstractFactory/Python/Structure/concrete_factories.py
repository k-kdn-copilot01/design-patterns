"""
Concrete Factories Implementation

This module contains concrete factory implementations that create
families of related products.
"""

from abstract_factory import AbstractFactory, AbstractProductA, AbstractProductB


# Concrete Products for Factory 1
class ConcreteProductA1(AbstractProductA):
    """Concrete Product A1 - variant 1 of product family A"""
    
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductB1(AbstractProductB):
    """Concrete Product B1 - variant 1 of product family B"""
    
    def useful_function_b(self) -> str:
        return "The result of the product B1."
    
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        """
        Product B1 can work correctly with Product A1.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


# Concrete Products for Factory 2
class ConcreteProductA2(AbstractProductA):
    """Concrete Product A2 - variant 2 of product family A"""
    
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class ConcreteProductB2(AbstractProductB):
    """Concrete Product B2 - variant 2 of product family B"""
    
    def useful_function_b(self) -> str:
        return "The result of the product B2."
    
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        """
        Product B2 can work correctly with Product A2.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


# Concrete Factories
class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factory 1 produces a family of products that belong to variant 1.
    The factory guarantees that resulting products are compatible.
    """
    
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Concrete Factory 2 produces a family of products that belong to variant 2.
    Each variant follows the same interface but implements different variants.
    """
    
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
