"""
Component: Base interface for objects that can have responsibilities added to them dynamically.
"""
from abc import ABC, abstractmethod


class Component(ABC):
    """Abstract base class defining the interface for objects that can be decorated."""
    
    @abstractmethod
    def operation(self) -> str:
        """Perform the base operation."""
        pass
