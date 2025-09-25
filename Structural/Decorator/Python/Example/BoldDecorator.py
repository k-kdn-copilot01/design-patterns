"""
BoldDecorator: Adds bold formatting to text.
"""
from TextDecorator import TextDecorator


class BoldDecorator(TextDecorator):
    """Decorator that adds bold formatting to text."""
    
    def format(self) -> str:
        """Add bold formatting to the text."""
        return f"**{self.text_component.format()}**"
