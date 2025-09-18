"""
GUI Factory - Real-world Abstract Factory Example

This example demonstrates the Abstract Factory pattern using GUI components
with different themes (Windows and MacOS style).
"""

from abc import ABC, abstractmethod


# Abstract Products
class Button(ABC):
    """Abstract button interface"""
    
    @abstractmethod
    def render(self) -> str:
        """Render the button"""
        pass
    
    @abstractmethod
    def click(self) -> str:
        """Handle button click"""
        pass


class Checkbox(ABC):
    """Abstract checkbox interface"""
    
    @abstractmethod
    def render(self) -> str:
        """Render the checkbox"""
        pass
    
    @abstractmethod
    def toggle(self) -> str:
        """Toggle checkbox state"""
        pass


class Window(ABC):
    """Abstract window interface"""
    
    @abstractmethod
    def render(self) -> str:
        """Render the window"""
        pass
    
    @abstractmethod
    def close(self) -> str:
        """Close the window"""
        pass


# Abstract Factory
class GUIFactory(ABC):
    """
    Abstract factory for creating GUI components.
    Each concrete factory will create components that match a specific theme.
    """
    
    @abstractmethod
    def create_button(self) -> Button:
        """Create a button component"""
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        """Create a checkbox component"""
        pass
    
    @abstractmethod
    def create_window(self) -> Window:
        """Create a window component"""
        pass
