"""
Main - Demonstrates the Facade pattern structure.
This file shows how the Facade pattern simplifies complex subsystem interactions.
"""

from Facade import Facade


def demonstrate_without_facade():
    """
    Demonstrate how complex it would be to work with subsystems directly.
    This shows the problem that the Facade pattern solves.
    """
    print("=" * 60)
    print("DEMONSTRATION: Working WITHOUT Facade (Complex)")
    print("=" * 60)
    
    # Import subsystems directly
    from SubsystemA import SubsystemA
    from SubsystemB import SubsystemB
    from SubsystemC import SubsystemC
    
    # Create instances manually
    subsystem_a = SubsystemA()
    subsystem_b = SubsystemB()
    subsystem_c = SubsystemC()
    
    print("Client: Working with subsystems directly...")
    print("-" * 40)
    
    # Client needs to know about all subsystems and their methods
    result_a = subsystem_a.complex_operation_a()
    result_b = subsystem_b.complex_operation_b()
    result_c = subsystem_c.complex_operation_c()
    
    print("-" * 40)
    print("Client: All operations completed manually")
    print(f"Results: {result_a}, {result_b}, {result_c}")
    print()


def demonstrate_with_facade():
    """
    Demonstrate how the Facade pattern simplifies subsystem interactions.
    This shows the solution that the Facade pattern provides.
    """
    print("=" * 60)
    print("DEMONSTRATION: Working WITH Facade (Simplified)")
    print("=" * 60)
    
    # Create Facade instance
    facade = Facade()
    
    print("Client: Working with Facade...")
    print("-" * 40)
    
    # Client only needs to know about the Facade
    simple_result = facade.simple_operation()
    print(f"Simple result: {simple_result}")
    print()
    
    complex_result = facade.complex_operation()
    print(f"Complex result: {complex_result}")
    print()
    
    # Demonstrate individual subsystem access through Facade
    print("Client: Accessing individual subsystems through Facade...")
    print("-" * 40)
    
    a_result = facade.subsystem_a_operation()
    b_result = facade.subsystem_b_operation()
    c_result = facade.subsystem_c_operation()
    
    print(f"Individual results: {a_result}, {b_result}, {c_result}")
    print()


def main():
    """
    Main function to demonstrate the Facade pattern.
    Shows both the problem (without Facade) and the solution (with Facade).
    """
    print("FACADE PATTERN DEMONSTRATION")
    print("=" * 60)
    print("The Facade pattern provides a unified interface to a set of")
    print("interfaces in a subsystem. It defines a higher-level interface")
    print("that makes the subsystem easier to use.")
    print()
    
    # Show the problem
    demonstrate_without_facade()
    
    # Show the solution
    demonstrate_with_facade()
    
    print("=" * 60)
    print("DEMONSTRATION COMPLETED")
    print("=" * 60)
    print()
    print("Key Benefits of Facade Pattern:")
    print("1. Simplifies complex subsystem interactions")
    print("2. Reduces coupling between client and subsystems")
    print("3. Provides a single entry point to a subsystem")
    print("4. Hides implementation details from clients")
    print("5. Makes the subsystem easier to use and understand")


if __name__ == "__main__":
    main()
