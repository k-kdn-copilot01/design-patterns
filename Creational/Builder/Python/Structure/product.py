class Product:
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration. Unlike in other creational
    patterns, different concrete builders can produce unrelated products.
    """
    
    def __init__(self):
        self.parts = []
    
    def add_part(self, part):
        """Add a part to the product"""
        self.parts.append(part)
    
    def list_parts(self):
        """List all parts of the product"""
        return f"Product parts: {', '.join(self.parts)}"
    
    def __str__(self):
        return self.list_parts()
