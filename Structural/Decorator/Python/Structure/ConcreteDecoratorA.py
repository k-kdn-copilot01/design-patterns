"""
ConcreteDecoratorA: Adds responsibilities to the component.
"""
from Decorator import Decorator


class ConcreteDecoratorA(Decorator):
    """Concrete decorator that adds behavior A."""
    
    def operation(self) -> str:
        """Add behavior A before calling the wrapped component."""
        return f"ConcreteDecoratorA({self.component.operation()})"
