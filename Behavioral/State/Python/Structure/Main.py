"""
State Pattern - Structure Demo
Demonstrates the basic State pattern implementation
"""

from state import Context
from concrete_states import ConcreteStateA


def main():
    """
    Main function to demonstrate the State pattern structure.
    """
    print("=== State Pattern Structure Demo ===\n")
    
    # Create context with initial state
    print("1. Creating context with initial state (ConcreteStateA)")
    context = Context(ConcreteStateA())
    print(f"   Current state: {type(context.get_state()).__name__}\n")
    
    # Make requests to demonstrate state transitions
    print("2. Making requests to demonstrate state transitions:")
    
    print("\n   Request 1:")
    context.request()
    print(f"   Current state: {type(context.get_state()).__name__}")
    
    print("\n   Request 2:")
    context.request()
    print(f"   Current state: {type(context.get_state()).__name__}")
    
    print("\n   Request 3:")
    context.request()
    print(f"   Current state: {type(context.get_state()).__name__}")
    
    print("\n   Request 4 (back to State A):")
    context.request()
    print(f"   Current state: {type(context.get_state()).__name__}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
