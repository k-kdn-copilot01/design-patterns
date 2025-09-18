"""
Abstract Factory Pattern - Structure Implementation

This module defines the abstract factory and product interfaces.
"""

from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """Abstract interface for product family A"""
    
    @abstractmethod
    def useful_function_a(self) -> str:
        """Return a result of the product A functionality"""
        pass


class AbstractProductB(ABC):
    """Abstract interface for product family B"""
    
    @abstractmethod
    def useful_function_b(self) -> str:
        """Return a result of the product B functionality"""
        pass
    
    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        """
        Product B can collaborate with Product A.
        Abstract Factory makes sure that all products it creates are compatible.
        """
        pass


class AbstractFactory(ABC):
    """
    Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept.
    """
    
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        """Create and return a product of type A"""
        pass
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        """Create and return a product of type B"""
        pass
