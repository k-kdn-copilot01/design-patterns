"""
Subject interface for Proxy pattern.
Defines the common interface for RealSubject and Proxy.
"""

from abc import ABC, abstractmethod


class Subject(ABC):
    """Abstract base class defining the interface for both RealSubject and Proxy."""
    
    @abstractmethod
    def request(self) -> str:
        """
        Abstract method that must be implemented by both RealSubject and Proxy.
        
        Returns:
            str: Result of the request operation
        """
        pass
