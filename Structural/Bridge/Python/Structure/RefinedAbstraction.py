"""
Bridge Pattern - Refined Abstraction
Extends the abstraction without changing the implementor.
"""

from Abstraction import Abstraction


class RefinedAbstraction(Abstraction):
    """
    You can extend the Abstraction without changing the Implementor classes.
    This allows for variations in the abstraction without affecting the
    implementation hierarchy.
    """
    
    def operation(self) -> str:
        """
        Extended operation that builds upon the base abstraction.
        
        Returns:
            str: Result of the refined operation
        """
        return f"RefinedAbstraction: Extended operation with:\n{self._implementor.operation_impl()}"
    
    def another_operation(self) -> str:
        """
        Additional operation specific to the refined abstraction.
        
        Returns:
            str: Result of another operation
        """
        return f"RefinedAbstraction: Another operation with:\n{self._implementor.operation_impl()}"
