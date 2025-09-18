from builder import Builder
from product import Product


class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have several
    variations of Builders, implemented differently.
    """
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset the builder to create a new product"""
        self._product = Product()
    
    def build_part_a(self):
        """Build part A for ConcreteBuilder1"""
        self._product.add_part("PartA1")
        return self
    
    def build_part_b(self):
        """Build part B for ConcreteBuilder1"""
        self._product.add_part("PartB1")
        return self
    
    def build_part_c(self):
        """Build part C for ConcreteBuilder1"""
        self._product.add_part("PartC1")
        return self
    
    def get_result(self):
        """Return the built product"""
        product = self._product
        self.reset()
        return product


class ConcreteBuilder2(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have several
    variations of Builders, implemented differently.
    """
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset the builder to create a new product"""
        self._product = Product()
    
    def build_part_a(self):
        """Build part A for ConcreteBuilder2"""
        self._product.add_part("PartA2")
        return self
    
    def build_part_b(self):
        """Build part B for ConcreteBuilder2"""
        self._product.add_part("PartB2")
        return self
    
    def build_part_c(self):
        """Build part C for ConcreteBuilder2"""
        self._product.add_part("PartC2")
        return self
    
    def get_result(self):
        """Return the built product"""
        product = self._product
        self.reset()
        return product
