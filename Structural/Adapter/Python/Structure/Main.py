"""
Main demo for Adapter pattern structure implementations.
Demonstrates the basic Adapter pattern with reference vs value comparison.
"""

from Target import Target
from Adaptee import Adaptee
from Adapter import Adapter
from Client import Client


def demonstrate_adapter_pattern():
    """
    Demonstrate the Adapter pattern with reference and value comparisons.
    """
    print("=== Structure Demo: Adapter Pattern ===\n")
    
    # Create Adaptee instance
    print("1. Creating Adaptee instance:")
    adaptee = Adaptee()
    print(f"Adaptee specific_request(): {adaptee.specific_request()}")
    print()
    
    # Create Adapter instance
    print("2. Creating Adapter instance:")
    adapter = Adapter(adaptee)
    print(f"Adapter request(): {adapter.request()}")
    print()
    
    # Demonstrate Client working with Target interface
    print("3. Client working with Adapter (Target interface):")
    client = Client(adapter)
    result = client.make_request()
    print(f"Client result: {result}")
    print()
    
    # Demonstrate reference vs value comparison
    print("4. Reference vs Value Comparison:")
    adaptee2 = Adaptee()
    adapter2 = Adapter(adaptee2)
    
    print(f"adaptee == adaptee2: {adaptee is adaptee2}")  # Different objects
    print(f"adapter == adapter2: {adapter is adapter2}")  # Different objects
    print(f"adaptee.specific_request() == adaptee2.specific_request(): {adaptee.specific_request() == adaptee2.specific_request()}")  # Same value
    print(f"adapter.request() == adapter2.request(): {adapter.request() == adapter2.request()}")  # Same value
    print()
    
    # Demonstrate that Adapter creates independent copies
    print("5. Independent Object Behavior:")
    print("Both adapters work independently:")
    print(f"Adapter 1: {adapter.request()}")
    print(f"Adapter 2: {adapter2.request()}")
    print()
    
    print("=== Structure Demo Complete ===")


if __name__ == "__main__":
    demonstrate_adapter_pattern()
