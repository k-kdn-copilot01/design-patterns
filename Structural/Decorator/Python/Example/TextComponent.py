"""
TextComponent: Base interface for text formatting.
"""
from abc import ABC, abstractmethod


class TextComponent(ABC):
    """Abstract base class for text components that can be formatted."""
    
    @abstractmethod
    def format(self) -> str:
        """Format and return the text."""
        pass
    
    @abstractmethod
    def get_plain_text(self) -> str:
        """Get the plain text without formatting."""
        pass
