"""
ColorDecorator: Adds color formatting to text.
"""
from TextDecorator import TextDecorator


class ColorDecorator(TextDecorator):
    """Decorator that adds color formatting to text."""
    
    def __init__(self, text_component: 'TextComponent', color: str):
        """Initialize with text component and color."""
        super().__init__(text_component)
        self._color = color
    
    def format(self) -> str:
        """Add color formatting to the text."""
        return f'<span style="color: {self._color}">{self.text_component.format()}</span>'
