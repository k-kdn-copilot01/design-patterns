from abstract_factory import AbstractFactory
from concrete_products import ConcreteProductA1, ConcreteProductA2, ConcreteProductB1, ConcreteProductB2

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()
