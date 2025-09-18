"""
Abstract Builder interface and Concrete Builder implementations.
"""

from abc import ABC, abstractmethod
from product import Product


class Builder(ABC):
    """
    Abstract Builder interface specifies methods for creating the different parts
    of the Product objects.
    """
    
    @property
    @abstractmethod
    def product(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_a(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_b(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps.
    """
    
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()
    
    def reset(self) -> None:
        self._product = Product()
    
    @property
    def product(self) -> Product:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).
        
        Usually, after returning the end result to the client, a builder instance
        is expected to be ready to start producing another product. That's why
        it's a usual practice to call the reset method at the end of the
        `getProduct` method body. However, this behavior is not mandatory, and
        you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product
    
    def produce_part_a(self) -> None:
        self._product.add_part("PartA1")
    
    def produce_part_b(self) -> None:
        self._product.add_part("PartB1")
    
    def produce_part_c(self) -> None:
        self._product.add_part("PartC1")


class ConcreteBuilder2(Builder):
    """
    Another Concrete Builder that produces a different variant of the product.
    """
    
    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self._product = Product()
    
    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product
    
    def produce_part_a(self) -> None:
        self._product.add_part("PartA2")
    
    def produce_part_b(self) -> None:
        self._product.add_part("PartB2")
    
    def produce_part_c(self) -> None:
        self._product.add_part("PartC2")
