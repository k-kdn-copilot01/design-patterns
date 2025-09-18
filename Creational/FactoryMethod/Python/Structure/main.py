"""
Main demonstration of Factory Method pattern structure.

This script demonstrates the basic structure and usage of the Factory Method pattern.
It shows how different concrete creators can create different concrete products
through the same factory method interface.
"""

from concrete_creators import ConcreteCreatorA, ConcreteCreatorB


def client_code(creator):
    """
    Client code that works with any creator through the base Creator interface.
    
    The client code doesn't need to know the specific creator or product classes.
    It works with creators and products through their abstract interfaces.
    
    Args:
        creator: A concrete creator instance.
    """
    print(f"Client: I'm not aware of the creator's class, but it still works.")
    print(f"{creator.some_operation()}", end="")


def demonstrate_factory_method():
    """
    Demonstrate the Factory Method pattern with different creators.
    """
    print("=== Factory Method Pattern Structure Demo ===\n")
    
    print("App: Launched with ConcreteCreatorA.")
    creator_a = ConcreteCreatorA()
    client_code(creator_a)
    print("\n")
    
    print("App: Launched with ConcreteCreatorB.")
    creator_b = ConcreteCreatorB()
    client_code(creator_b)
    print("\n")
    
    # Demonstrate direct product creation and usage
    print("=== Direct Product Creation Demo ===")
    product_a = creator_a.factory_method()
    product_b = creator_b.factory_method()
    
    print(f"Product A Info: {product_a.get_info()}")
    print(f"Product A Operation: {product_a.operation()}")
    print()
    
    print(f"Product B Info: {product_b.get_info()}")
    print(f"Product B Operation: {product_b.operation()}")
    print()


def demonstrate_flexibility():
    """
    Demonstrate the flexibility of the Factory Method pattern.
    """
    print("=== Flexibility Demo ===")
    
    creators = [ConcreteCreatorA(), ConcreteCreatorB()]
    
    for i, creator in enumerate(creators, 1):
        print(f"\nUsing Creator {i}:")
        product = creator.factory_method()
        print(f"  Created: {product.get_info()}")
        print(f"  Operation: {product.operation()}")


def main():
    """
    Main function to run all demonstrations.
    """
    demonstrate_factory_method()
    demonstrate_flexibility()
    
    print("\n=== Factory Method Structure Demo Complete ===")


if __name__ == "__main__":
    main()
