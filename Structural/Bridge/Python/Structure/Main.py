"""
Bridge Pattern - Structure Demo
Demonstrates the basic structure of the Bridge pattern.
"""

from Abstraction import Abstraction
from RefinedAbstraction import RefinedAbstraction
from ConcreteImplementorA import ConcreteImplementorA
from ConcreteImplementorB import ConcreteImplementorB


def main():
    """
    Demo function showing the Bridge pattern structure.
    """
    print("=== Bridge Pattern Structure Demo ===\n")
    
    # Create concrete implementors
    implementor_a = ConcreteImplementorA()
    implementor_b = ConcreteImplementorB()
    
    print("1. Testing Abstraction with ConcreteImplementorA:")
    abstraction_a = Abstraction(implementor_a)
    print(abstraction_a.operation())
    print()
    
    print("2. Testing Abstraction with ConcreteImplementorB:")
    abstraction_b = Abstraction(implementor_b)
    print(abstraction_b.operation())
    print()
    
    print("3. Testing RefinedAbstraction with ConcreteImplementorA:")
    refined_abstraction_a = RefinedAbstraction(implementor_a)
    print(refined_abstraction_a.operation())
    print()
    print("   Testing another operation:")
    print(refined_abstraction_a.another_operation())
    print()
    
    print("4. Testing RefinedAbstraction with ConcreteImplementorB:")
    refined_abstraction_b = RefinedAbstraction(implementor_b)
    print(refined_abstraction_b.operation())
    print()
    print("   Testing another operation:")
    print(refined_abstraction_b.another_operation())
    print()
    
    print("=== Bridge Pattern Structure Demo Complete ===")


if __name__ == "__main__":
    main()
