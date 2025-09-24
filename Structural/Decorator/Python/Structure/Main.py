"""
Main: Demonstrates the Decorator pattern with various combinations.
"""
from ConcreteComponent import ConcreteComponent
from ConcreteDecoratorA import ConcreteDecoratorA
from ConcreteDecoratorB import ConcreteDecoratorB


def main():
    """Demonstrate the Decorator pattern."""
    print("=== Decorator Pattern Demo ===\n")
    
    # Create a concrete component
    component = ConcreteComponent()
    print(f"1. Basic component: {component.operation()}")
    
    # Decorate with ConcreteDecoratorA
    decorator_a = ConcreteDecoratorA(component)
    print(f"2. With DecoratorA: {decorator_a.operation()}")
    
    # Decorate with ConcreteDecoratorB
    decorator_b = ConcreteDecoratorB(component)
    print(f"3. With DecoratorB: {decorator_b.operation()}")
    
    # Decorate with both decorators (A then B)
    decorator_ab = ConcreteDecoratorB(ConcreteDecoratorA(component))
    print(f"4. With DecoratorA + DecoratorB: {decorator_ab.operation()}")
    
    # Decorate with both decorators (B then A)
    decorator_ba = ConcreteDecoratorA(ConcreteDecoratorB(component))
    print(f"5. With DecoratorB + DecoratorA: {decorator_ba.operation()}")
    
    # Multiple layers of the same decorator
    decorator_aa = ConcreteDecoratorA(ConcreteDecoratorA(component))
    print(f"6. With DecoratorA + DecoratorA: {decorator_aa.operation()}")
    
    print("\n=== Pattern Benefits ===")
    print("- Dynamic behavior addition without altering existing code")
    print("- Flexible combination of behaviors")
    print("- Single Responsibility Principle compliance")
    print("- Open/Closed Principle compliance")


if __name__ == "__main__":
    main()
