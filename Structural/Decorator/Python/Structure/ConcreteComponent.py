"""
ConcreteComponent: Defines an object to which additional responsibilities can be attached.
"""
from Component import Component


class ConcreteComponent(Component):
    """Concrete implementation of Component."""
    
    def operation(self) -> str:
        """Return the basic operation result."""
        return "ConcreteComponent"
