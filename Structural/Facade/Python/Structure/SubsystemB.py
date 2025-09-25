"""
SubsystemB - Another part of the complex subsystem that the Facade will simplify.
This represents another component of a larger, more complex system.
"""

class SubsystemB:
    """Another complex subsystem component that performs specific operations."""
    
    def operation_b1(self):
        """Perform operation B1 of the subsystem."""
        print("SubsystemB: Performing operation B1")
        return "Result from B1"
    
    def operation_b2(self):
        """Perform operation B2 of the subsystem."""
        print("SubsystemB: Performing operation B2")
        return "Result from B2"
    
    def complex_operation_b(self):
        """Perform a complex operation that involves multiple steps."""
        print("SubsystemB: Starting complex operation B")
        result1 = self.operation_b1()
        result2 = self.operation_b2()
        print("SubsystemB: Complex operation B completed")
        return f"Complex B result: {result1}, {result2}"
