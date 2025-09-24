"""
SubsystemA - Part of the complex subsystem that the Facade will simplify.
This represents one component of a larger, more complex system.
"""

class SubsystemA:
    """A complex subsystem component that performs specific operations."""
    
    def operation_a1(self):
        """Perform operation A1 of the subsystem."""
        print("SubsystemA: Performing operation A1")
        return "Result from A1"
    
    def operation_a2(self):
        """Perform operation A2 of the subsystem."""
        print("SubsystemA: Performing operation A2")
        return "Result from A2"
    
    def complex_operation_a(self):
        """Perform a complex operation that involves multiple steps."""
        print("SubsystemA: Starting complex operation A")
        result1 = self.operation_a1()
        result2 = self.operation_a2()
        print("SubsystemA: Complex operation A completed")
        return f"Complex A result: {result1}, {result2}"
