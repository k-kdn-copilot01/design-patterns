"""
ConcreteDecoratorB: Adds responsibilities to the component.
"""
from Decorator import Decorator


class ConcreteDecoratorB(Decorator):
    """Concrete decorator that adds behavior B."""
    
    def operation(self) -> str:
        """Add behavior B before calling the wrapped component."""
        return f"ConcreteDecoratorB({self.component.operation()})"
