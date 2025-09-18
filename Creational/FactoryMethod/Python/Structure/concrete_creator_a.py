from creator import Creator
from concrete_product_a import ConcreteProductA

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()
