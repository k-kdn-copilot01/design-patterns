"""
SubsystemC - Third part of the complex subsystem that the Facade will simplify.
This represents another component of a larger, more complex system.
"""

class SubsystemC:
    """Third complex subsystem component that performs specific operations."""
    
    def operation_c1(self):
        """Perform operation C1 of the subsystem."""
        print("SubsystemC: Performing operation C1")
        return "Result from C1"
    
    def operation_c2(self):
        """Perform operation C2 of the subsystem."""
        print("SubsystemC: Performing operation C2")
        return "Result from C2"
    
    def complex_operation_c(self):
        """Perform a complex operation that involves multiple steps."""
        print("SubsystemC: Starting complex operation C")
        result1 = self.operation_c1()
        result2 = self.operation_c2()
        print("SubsystemC: Complex operation C completed")
        return f"Complex C result: {result1}, {result2}"
