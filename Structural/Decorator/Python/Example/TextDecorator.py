"""
TextDecorator: Base decorator for text formatting.
"""
from TextComponent import TextComponent


class TextDecorator(TextComponent):
    """Base decorator class for text formatting."""
    
    def __init__(self, text_component: TextComponent):
        """Initialize decorator with a text component."""
        self._text_component = text_component
    
    @property
    def text_component(self) -> TextComponent:
        """Get the wrapped text component."""
        return self._text_component
    
    def format(self) -> str:
        """Delegate to the wrapped text component."""
        return self._text_component.format()
    
    def get_plain_text(self) -> str:
        """Get plain text from the wrapped component."""
        return self._text_component.get_plain_text()
