from abstract_factory import AbstractFactory
from abstract_products import AbstractProductA, AbstractProductB


class Client:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any
    factory or product subclass to the client code without breaking it.
    """
    
    def __init__(self, factory: AbstractFactory):
        self.factory = factory
        self.product_a = None
        self.product_b = None
    
    def create_products(self):
        """Create products using the factory"""
        self.product_a = self.factory.create_product_a()
        self.product_b = self.factory.create_product_b()
    
    def use_products(self):
        """Use the created products"""
        if self.product_a and self.product_b:
            print(self.product_b.useful_function_b())
            print(self.product_b.another_useful_function_b(self.product_a))
        else:
            print("Products not created yet. Call create_products() first.")
