"""
Decorator: Maintains a reference to a Component object and defines an interface
that conforms to Component's interface.
"""
from Component import Component


class Decorator(Component):
    """Base decorator class that maintains a reference to a Component."""
    
    def __init__(self, component: Component):
        """Initialize decorator with a component."""
        self._component = component
    
    @property
    def component(self) -> Component:
        """Get the wrapped component."""
        return self._component
    
    def operation(self) -> str:
        """Delegate to the wrapped component."""
        return self._component.operation()
