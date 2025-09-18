"""
Product class that represents the complex object being built.
"""

class Product:
    """
    The Product class represents a complex object that is being constructed.
    It contains multiple parts that are added by different builders.
    """
    
    def __init__(self):
        self.parts = []
    
    def add_part(self, part: str):
        """Add a part to the product."""
        self.parts.append(part)
    
    def list_parts(self) -> str:
        """List all parts of the product."""
        return f"Product parts: {', '.join(self.parts)}"
    
    def __str__(self):
        return self.list_parts()
