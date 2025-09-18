from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are
    usually able to collaborate among themselves.
    """
    
    @abstractmethod
    def create_product_a(self):
        """Create Product A"""
        pass
    
    @abstractmethod
    def create_product_b(self):
        """Create Product B"""
        pass
