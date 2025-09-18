from abc import ABC, abstractmethod


class Button(ABC):
    """Abstract Button component"""
    
    @abstractmethod
    def render(self) -> str:
        """Render the button"""
        pass
    
    @abstractmethod
    def click(self) -> str:
        """Handle button click"""
        pass


class Dialog(ABC):
    """Abstract Dialog component"""
    
    @abstractmethod
    def render(self) -> str:
        """Render the dialog"""
        pass
    
    @abstractmethod
    def show(self) -> str:
        """Show the dialog"""
        pass


class TextField(ABC):
    """Abstract TextField component"""
    
    @abstractmethod
    def render(self) -> str:
        """Render the text field"""
        pass
    
    @abstractmethod
    def get_text(self) -> str:
        """Get text from the field"""
        pass
