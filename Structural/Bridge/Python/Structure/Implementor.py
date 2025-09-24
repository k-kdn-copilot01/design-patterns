"""
Bridge Pattern - Implementor Interface
Defines the interface for implementation classes.
"""

from abc import ABC, abstractmethod


class Implementor(ABC):
    """
    The Implementor interface declares methods common to all concrete implementations.
    It doesn't have to match the Abstraction's interface. In fact, the two interfaces
    can be completely different. Typically the Implementor interface provides only
    primitive operations, while the Abstraction defines higher-level operations
    based on those primitives.
    """
    
    @abstractmethod
    def operation_impl(self) -> str:
        """
        Primitive operation that will be implemented by concrete classes.
        
        Returns:
            str: Result of the operation
        """
        pass
