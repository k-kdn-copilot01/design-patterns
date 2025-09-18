"""
Builder Pattern - Structure Demo

This demonstrates the core structure of the Builder pattern:
- Builder: Abstract interface for building products
- ConcreteBuilder: Specific implementations of the builder
- Product: The complex object being built
- Director: Orchestrates the building process
- Client: Uses the pattern to create products

Run this file to see the Builder pattern in action.
"""

from client import Client


def main():
    """Main function to run the Builder pattern demo"""
    print("Builder Pattern - Structure Demo")
    print("=" * 40)
    print()
    
    client = Client()
    client.demonstrate_builder_pattern()


if __name__ == "__main__":
    main()
