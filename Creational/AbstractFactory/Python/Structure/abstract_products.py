from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
    Abstract Product A declares the interface for a type of product object.
    """
    
    @abstractmethod
    def useful_function_a(self) -> str:
        """Useful function A"""
        pass


class AbstractProductB(ABC):
    """
    Abstract Product B declares the interface for a type of product object.
    """
    
    @abstractmethod
    def useful_function_b(self) -> str:
        """Useful function B"""
        pass
    
    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        """Another useful function B that collaborates with Product A"""
        pass
