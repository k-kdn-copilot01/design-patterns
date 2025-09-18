from abc import ABC, abstractmethod
from product import Product

class Builder(ABC):
    @abstractmethod
    def build_part_a(self): pass

    @abstractmethod
    def build_part_b(self): pass

    @abstractmethod
    def get_result(self) -> Product: pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("PartA1")

    def build_part_b(self):
        self.product.add("PartB1")

    def get_result(self) -> Product:
        return self.product


class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("PartA2")

    def build_part_b(self):
        self.product.add("PartB2")

    def get_result(self) -> Product:
        return self.product
