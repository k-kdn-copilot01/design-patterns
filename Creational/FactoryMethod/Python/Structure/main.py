"""
Main demonstration of the Factory Method pattern structure
"""
from client import Client
from concrete_creators import ConcreteCreatorA, ConcreteCreatorB


def main():
    """
    Demonstrate the Factory Method pattern with different creators
    """
    print("Factory Method Pattern - Structure Demo")
    print("=" * 50)
    
    # Work with ConcreteCreatorA
    print("\n1. Working with ConcreteCreatorA:")
    creator_a = ConcreteCreatorA()
    Client.client_code(creator_a)
    
    print("\n" + "-" * 30)
    
    # Work with ConcreteCreatorB
    print("\n2. Working with ConcreteCreatorB:")
    creator_b = ConcreteCreatorB()
    Client.client_code(creator_b)
    
    print("\n" + "=" * 50)
    print("Demo completed successfully!")


if __name__ == "__main__":
    main()
