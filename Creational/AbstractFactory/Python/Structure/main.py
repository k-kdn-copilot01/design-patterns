"""
Abstract Factory Pattern Structure Demo

This demo shows the basic structure of the Abstract Factory pattern
with abstract factories, concrete factories, and product families.
"""

from abstract_factory import AbstractFactory
from concrete_factories import ConcreteFactory1, ConcreteFactory2
from client import Client, client_code


def main():
    """Main function demonstrating Abstract Factory pattern structure"""
    print("=== Structure Demo: Abstract Factory Pattern ===\n")
    
    # Demo 1: Using factory 1
    print("1. Using ConcreteFactory1:")
    factory1 = ConcreteFactory1()
    client_code(factory1)
    print()
    
    # Demo 2: Using factory 2
    print("2. Using ConcreteFactory2:")
    factory2 = ConcreteFactory2()
    client_code(factory2)
    print()
    
    # Demo 3: Using Client class
    print("3. Using Client class with different factories:")
    
    client1 = Client(ConcreteFactory1())
    client1.run()
    
    client2 = Client(ConcreteFactory2())
    client2.run()
    
    print("=== Structure Demo Complete ===")


if __name__ == "__main__":
    main()
