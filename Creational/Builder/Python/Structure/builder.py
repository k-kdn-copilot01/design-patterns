from abc import ABC, abstractmethod


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts
    of the Product objects.
    """
    
    @abstractmethod
    def build_part_a(self):
        """Build part A of the product"""
        pass
    
    @abstractmethod
    def build_part_b(self):
        """Build part B of the product"""
        pass
    
    @abstractmethod
    def build_part_c(self):
        """Build part C of the product"""
        pass
    
    @abstractmethod
    def get_result(self):
        """Return the built product"""
        pass
