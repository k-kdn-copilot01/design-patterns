from creator import Creator
from concrete_product_b import ConcreteProductB

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()
