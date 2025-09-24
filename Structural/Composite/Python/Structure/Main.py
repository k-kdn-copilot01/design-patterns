from Component import Component
from Leaf import Leaf
from Composite import Composite


def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """
    print(f"RESULT: {component.operation()}")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple or
    complex, without depending on their concrete classes.
    """
    if component1.is_composite():
        component1.add(component2)
    
    print(f"RESULT: {component1.operation()}")


def main():
    print("=== Structure Demo: Composite Pattern ===\n")
    
    # This way the client code can support the simple leaf components...
    print("1. Simple Leaf Components:")
    leaf1 = Leaf("Leaf1")
    leaf2 = Leaf("Leaf2")
    client_code(leaf1)
    client_code(leaf2)
    print()
    
    # ...as well as the complex composites.
    print("2. Complex Composite Components:")
    tree = Composite("Tree")
    branch1 = Composite("Branch1")
    branch2 = Composite("Branch2")
    
    # Build the tree structure
    branch1.add(Leaf("Leaf1"))
    branch1.add(Leaf("Leaf2"))
    branch2.add(Leaf("Leaf3"))
    
    tree.add(branch1)
    tree.add(branch2)
    
    client_code(tree)
    print()
    
    # Demonstrate adding components dynamically
    print("3. Dynamic Component Addition:")
    leaf4 = Leaf("Leaf4")
    client_code2(tree, leaf4)
    print()
    
    # Show the tree structure
    print("4. Tree Structure Analysis:")
    print(f"Tree is composite: {tree.is_composite()}")
    print(f"Tree children count: {len(tree.get_children())}")
    print(f"Branch1 children count: {len(branch1.get_children())}")
    print(f"Branch2 children count: {len(branch2.get_children())}")
    
    print("\n=== Structure Demo Complete ===")


if __name__ == "__main__":
    main()
