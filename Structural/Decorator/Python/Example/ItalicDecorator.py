"""
ItalicDecorator: Adds italic formatting to text.
"""
from TextDecorator import TextDecorator


class ItalicDecorator(TextDecorator):
    """Decorator that adds italic formatting to text."""
    
    def format(self) -> str:
        """Add italic formatting to the text."""
        return f"*{self.text_component.format()}*"
