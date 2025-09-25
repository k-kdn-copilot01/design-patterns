"""
UnderlineDecorator: Adds underline formatting to text.
"""
from TextDecorator import TextDecorator


class UnderlineDecorator(TextDecorator):
    """Decorator that adds underline formatting to text."""
    
    def format(self) -> str:
        """Add underline formatting to the text."""
        return f"<u>{self.text_component.format()}</u>"
