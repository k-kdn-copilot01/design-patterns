"""
Facade - Provides a simplified interface to a complex subsystem.
The Facade pattern provides a unified interface to a set of interfaces in a subsystem.
"""

from SubsystemA import SubsystemA
from SubsystemB import SubsystemB
from SubsystemC import SubsystemC


class Facade:
    """
    The Facade class provides a simplified interface to the complex subsystem.
    It knows which subsystem classes are responsible for a request and delegates
    client requests to appropriate subsystem objects.
    """
    
    def __init__(self):
        """Initialize the Facade with subsystem instances."""
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()
    
    def simple_operation(self):
        """
        Provide a simple operation that hides the complexity of the subsystem.
        This method demonstrates how the Facade simplifies complex operations.
        """
        print("Facade: Starting simple operation")
        print("=" * 50)
        
        # Use individual operations from subsystems
        result_a = self._subsystem_a.operation_a1()
        result_b = self._subsystem_b.operation_b1()
        result_c = self._subsystem_c.operation_c1()
        
        print("=" * 50)
        print("Facade: Simple operation completed")
        return f"Simple operation results: {result_a}, {result_b}, {result_c}"
    
    def complex_operation(self):
        """
        Provide a complex operation that coordinates multiple subsystems.
        This method demonstrates how the Facade can orchestrate complex workflows.
        """
        print("Facade: Starting complex operation")
        print("=" * 50)
        
        # Coordinate complex operations from all subsystems
        result_a = self._subsystem_a.complex_operation_a()
        result_b = self._subsystem_b.complex_operation_b()
        result_c = self._subsystem_c.complex_operation_c()
        
        print("=" * 50)
        print("Facade: Complex operation completed")
        return f"Complex operation results: {result_a}, {result_b}, {result_c}"
    
    def subsystem_a_operation(self):
        """Provide access to SubsystemA through the Facade."""
        print("Facade: Delegating to SubsystemA")
        return self._subsystem_a.complex_operation_a()
    
    def subsystem_b_operation(self):
        """Provide access to SubsystemB through the Facade."""
        print("Facade: Delegating to SubsystemB")
        return self._subsystem_b.complex_operation_b()
    
    def subsystem_c_operation(self):
        """Provide access to SubsystemC through the Facade."""
        print("Facade: Delegating to SubsystemC")
        return self._subsystem_c.complex_operation_c()
