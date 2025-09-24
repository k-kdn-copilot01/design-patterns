"""
Target interface that defines the domain-specific interface that Client uses.
"""
from abc import ABC, abstractmethod


class Target(ABC):
    """
    The Target defines the domain-specific interface used by the client code.
    """
    
    @abstractmethod
    def request(self) -> str:
        """
        The default behavior of the Target.
        """
        pass
