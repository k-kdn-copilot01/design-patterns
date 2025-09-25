"""
Bridge Pattern - Abstraction
Defines the abstraction's interface and maintains a reference to an object
of type Implementor.
"""

from Implementor import Implementor


class Abstraction:
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the Implementor
    hierarchy and delegates all of the real work to this object.
    """
    
    def __init__(self, implementor: Implementor):
        """
        Initialize the abstraction with an implementor.
        
        Args:
            implementor (Implementor): The concrete implementor to use
        """
        self._implementor = implementor
    
    def operation(self) -> str:
        """
        The Abstraction may define operations that are based on those
        implemented by the Implementor.
        
        Returns:
            str: Result of the operation
        """
        return f"Abstraction: Base operation with:\n{self._implementor.operation_impl()}"
