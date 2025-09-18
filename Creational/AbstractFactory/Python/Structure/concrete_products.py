from abstract_product import AbstractProductA, AbstractProductB

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "ProductA1"

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "ProductA2"

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "ProductB1"

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "ProductB2"
