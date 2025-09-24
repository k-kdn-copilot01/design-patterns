"""
Bridge Pattern - Structure Package
Core classes demonstrating the Bridge pattern structure.
"""

from .Implementor import Implementor
from .ConcreteImplementorA import ConcreteImplementorA
from .ConcreteImplementorB import ConcreteImplementorB
from .Abstraction import Abstraction
from .RefinedAbstraction import RefinedAbstraction

__all__ = [
    'Implementor',
    'ConcreteImplementorA', 
    'ConcreteImplementorB',
    'Abstraction',
    'RefinedAbstraction'
]
