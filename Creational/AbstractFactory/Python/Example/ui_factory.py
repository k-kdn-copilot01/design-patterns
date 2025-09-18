from abc import ABC, abstractmethod


class UIFactory(ABC):
    """
    Abstract Factory for creating UI components.
    Each concrete factory creates a family of UI components with a specific theme.
    """
    
    @abstractmethod
    def create_button(self):
        """Create a button component"""
        pass
    
    @abstractmethod
    def create_dialog(self):
        """Create a dialog component"""
        pass
    
    @abstractmethod
    def create_text_field(self):
        """Create a text field component"""
        pass
