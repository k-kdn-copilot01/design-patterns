"""
Client Code for Abstract Factory Pattern

The client code works with factories and products only through abstract types:
AbstractFactory and AbstractProduct. This lets you pass any factory or product
subclass to the client code without breaking it.
"""

from abstract_factory import AbstractFactory


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with any concrete factory class.
    It doesn't care which concrete factory it gets, as long as
    it can work with its products via the abstract interface.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    
    print(product_b.useful_function_b())
    print(product_b.another_useful_function_b(product_a))


class Client:
    """
    Client class that demonstrates working with abstract factories
    """
    
    def __init__(self, factory: AbstractFactory):
        self.factory = factory
    
    def run(self) -> None:
        """Execute client logic using the provided factory"""
        print(f"Client: Working with {self.factory.__class__.__name__}")
        
        # Create products using the factory
        product_a = self.factory.create_product_a()
        product_b = self.factory.create_product_b()
        
        # Use the products
        print(f"Product A: {product_a.useful_function_a()}")
        print(f"Product B: {product_b.useful_function_b()}")
        print(f"Collaboration: {product_b.another_useful_function_b(product_a)}")
        print()
