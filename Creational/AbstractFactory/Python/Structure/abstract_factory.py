from abc import ABC, abstractmethod
from abstract_product import AbstractProductA, AbstractProductB

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA: pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB: pass
