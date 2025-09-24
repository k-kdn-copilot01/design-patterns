"""
Bridge Pattern - Concrete Implementor A
Concrete implementation of the Implementor interface.
"""

from Implementor import Implementor


class ConcreteImplementorA(Implementor):
    """
    Each Concrete Implementor contains a specific implementation of the
    Implementor interface. The implementation can be different for each
    concrete class.
    """
    
    def operation_impl(self) -> str:
        """
        Concrete implementation of the operation.
        
        Returns:
            str: Result specific to ConcreteImplementorA
        """
        return "ConcreteImplementorA: Here's the result on the platform A."
