"""
Bridge Pattern - Concrete Implementor B
Another concrete implementation of the Implementor interface.
"""

from Implementor import Implementor


class ConcreteImplementorB(Implementor):
    """
    Each Concrete Implementor contains a specific implementation of the
    Implementor interface. The implementation can be different for each
    concrete class.
    """
    
    def operation_impl(self) -> str:
        """
        Concrete implementation of the operation.
        
        Returns:
            str: Result specific to ConcreteImplementorB
        """
        return "ConcreteImplementorB: Here's the result on the platform B."
