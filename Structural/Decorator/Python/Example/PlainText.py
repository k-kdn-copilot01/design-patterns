"""
PlainText: Basic text component without any formatting.
"""
from TextComponent import TextComponent


class PlainText(TextComponent):
    """Concrete implementation of TextComponent for plain text."""
    
    def __init__(self, text: str):
        """Initialize with plain text."""
        self._text = text
    
    def format(self) -> str:
        """Return the plain text without any formatting."""
        return self._text
    
    def get_plain_text(self) -> str:
        """Return the plain text."""
        return self._text
